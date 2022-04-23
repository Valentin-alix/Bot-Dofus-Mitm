from shutil import move
from threading import Timer
from time import sleep
from time import perf_counter
from com.ankamagames.atouin.messages.EntityMovementCompleteMessage import (
    EntityMovementCompleteMessage,
)
from com.ankamagames.atouin.messages.EntityMovementStoppedMessage import (
    EntityMovementStoppedMessage,
)
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.game.common.managers.MapMovementAdapter import (
    MapMovementAdapter,
)
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.roleplay.actions.PlayerFightRequestAction import (
    PlayerFightRequestAction,
)

# from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import RoleplayEntitiesFrame
from com.ankamagames.dofus.logic.game.roleplay.messages.CharacterMovementStoppedMessage import (
    CharacterMovementStoppedMessage,
)
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import (
    PlayerLifeStatusEnum,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementCancelMessage import (
    GameMapMovementCancelMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementConfirmMessage import (
    GameMapMovementConfirmMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import (
    GameMapMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementRequestMessage import (
    GameMapMovementRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapNoMovementMessage import (
    GameMapNoMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.ChangeMapMessage import (
    ChangeMapMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import (
    MapComplementaryInformationsDataMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.TeleportOnSameMapMessage import (
    TeleportOnSameMapMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionFinishedMessage import (
    GameRolePlayDelayedActionFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayAttackMonsterRequestMessage import (
    GameRolePlayAttackMonsterRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayFightRequestCanceledMessage import (
    GameRolePlayFightRequestCanceledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.EditHavenBagFinishedMessage import (
    EditHavenBagFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import (
    LeaveDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersHelpersLeaveMessage import (
    GuildFightPlayersHelpersLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseEndedMessage import (
    InteractiveUseEndedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseErrorMessage import (
    InteractiveUseErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import (
    InteractiveUseRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUsedMessage import (
    InteractiveUsedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.skill.InteractiveUseWithParamRequestMessage import (
    InteractiveUseWithParamRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import (
    ExchangeLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightDefenderLeaveMessage import (
    PrismFightDefenderLeaveMessage,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import (
    InteractiveElement,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.handlers.messages.Action import Action
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.pathfinding.Pathfinding import Pathfinding
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MovementPath import MovementPath

logger = Logger(__name__)


class RoleplayMovementFrame(Frame):
    CONSECUTIVE_MOVEMENT_DELAY: int = 0.25

    _wantToChangeMap: float = -1

    _changeMapByAutoTrip: bool = False

    _followingMove: MapPoint

    _followingIe: object

    _followingMonsterGroup: object

    _followingMessage = None

    _isRequestingMovement: bool

    _latestMovementRequest: int

    _destinationPoint: int

    _nextMovementBehavior: int

    _lastPlayerValidatedPosition: MapPoint

    _lastMoveEndCellId: int

    _canMove: bool = True

    _mapHasAggressiveMonsters: bool = False

    def __init__(self):
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    @property
    def isRequestingMovement(self) -> bool:
        return self._isRequestingMovement

    def pushed(self) -> bool:
        self._wantToChangeMap = -1
        self._changeMapByAutoTrip = False
        self._followingIe = None
        self._followingMonsterGroup = None
        self._followingMove = None
        self._isRequestingMovement = False
        self._latestMovementRequest = 0
        self._lastMoveEndCellId = None
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, GameMapNoMovementMessage):
            logger.debug("Map change impossible")
            self._isRequestingMovement = False
            if self._followingIe:
                self.activateSkill(
                    self._followingIe.skillInstanceId,
                    self._followingIe.ie,
                    self._followingIe.additionalParam,
                )
                self._followingIe = None
            if self._followingMonsterGroup:
                self.requestMonsterFight(self._followingMonsterGroup.id)
                self._followingMonsterGroup = None
            else:
                gmnmm = msg
                newPos = MapPoint.fromCoords(gmnmm.cellX, gmnmm.cellY)
                player: AnimatedCharacter = DofusEntities.getEntity(
                    PlayedCharacterManager().id
                )
                if not player:
                    return True
                if player.isMoving:
                    player.stop = True
                player.position = newPos
            return True

        if isinstance(msg, GameMapMovementMessage):
            gmmmsg = msg
            movedEntity = DofusEntities.getEntity(gmmmsg.actorId)
            clientMovePath = MapMovementAdapter.getClientMovement(gmmmsg.keyMovements)
            if movedEntity:
                movedEntity.position.cellId = clientMovePath.end.cellId
            if gmmmsg.actorId != PlayedCharacterManager().id:
                self.applyGameMapMovement(gmmmsg.actorId, clientMovePath, msg)
            else:
                self._isRequestingMovement = False
                pathDuration = max(1, clientMovePath.getCrossingDuration())
                logger.debug(
                    "Sending Entity movement complete in %s seconds", pathDuration
                )
                Timer(
                    1.5 * pathDuration,
                    lambda: Kernel()
                    .getWorker()
                    .processImmediately(EntityMovementCompleteMessage(movedEntity)),
                ).start()
            return True

        if isinstance(msg, EntityMovementCompleteMessage):
            emcmsg = msg
            if emcmsg.entity.id == PlayedCharacterManager().id:
                gmmcmsg = GameMapMovementConfirmMessage()
                ConnectionsHandler.getConnection().send(gmmcmsg)
                if (
                    self._wantToChangeMap >= 0
                    and emcmsg.entity.position.cellId == self._destinationPoint
                ):
                    logger.debug(
                        "Player arrived at destination point and he wanted to change map"
                    )
                    self.askMapChange()
                    self._isRequestingMovement = False
                if self._followingIe:
                    self.activateSkill(
                        self._followingIe.skillInstanceId,
                        self._followingIe.ie,
                        self._followingIe.additionalParam,
                    )
                    self._followingIe = None
                if self._followingMonsterGroup:
                    self.requestMonsterFight(self._followingMonsterGroup.id)
                    self._followingMonsterGroup = None
                Kernel().getWorker().processImmediately(
                    CharacterMovementStoppedMessage()
                )
            return True

        if isinstance(msg, EntityMovementStoppedMessage):
            emsmsg = msg
            if emsmsg.entity.id == PlayedCharacterManager().id:
                canceledMoveMessage = GameMapMovementCancelMessage()
                canceledMoveMessage.init(emsmsg.entity.position.cellId)
                ConnectionsHandler.getConnection().send(canceledMoveMessage)
                self._isRequestingMovement = False
                if self._followingMove and self._canMove:
                    self.askMoveTo(self._followingMove)
                    self._followingMove = None
                if self._followingMessage:
                    if isinstance(self._followingMessage, PlayerFightRequestAction):
                        Kernel().getWorker().process(self._followingMessage)
                    else:
                        ConnectionsHandler.getConnection().send(self._followingMessage)
                    self._followingMessage = None
            return True

        if isinstance(msg, TeleportOnSameMapMessage):
            tosmmsg = msg
            teleportedEntity = DofusEntities.getEntity(tosmmsg.targetId)
            if teleportedEntity:
                if isinstance(teleportedEntity, IMovable):
                    if teleportedEntity.isMoving:
                        teleportedEntity.stop(True)
                    teleportedEntity
                else:
                    logger.warn("Cannot teleport a non IMovable entity. WTF ?")
            else:
                logger.warn(
                    "Received a teleportation request for a non-existing entity. Aborting."
                )
            return True

        if isinstance(msg, InteractiveUsedMessage):
            if msg.entityId == PlayedCharacterManager().id:
                self._canMove = msg.canMove
            return True

        if isinstance(msg, InteractiveUseEndedMessage):
            self._canMove = True
            return True

        if isinstance(msg, InteractiveUseErrorMessage):
            self._canMove = True
            return True

        if isinstance(msg, LeaveDialogMessage):
            self._canMove = True
            return False

        if isinstance(msg, ExchangeLeaveMessage):
            self._canMove = True
            return False

        if isinstance(msg, EditHavenBagFinishedMessage):
            self._canMove = True
            return False

        if isinstance(msg, GameRolePlayDelayedActionFinishedMessage):
            if msg.delayedCharacterId == PlayedCharacterManager().id:
                self._canMove = True
            return False

        if isinstance(msg, GuildFightPlayersHelpersLeaveMessage):
            if msg.playerId == PlayedCharacterManager().id:
                self._canMove = True
            return False

        if isinstance(msg, PrismFightDefenderLeaveMessage):
            if msg.fighterToRemoveId == PlayedCharacterManager().id:
                self._canMove = True
            return False

        if isinstance(msg, GameRolePlayFightRequestCanceledMessage):
            if (
                msg.targetId == PlayedCharacterManager().id
                or msg.sourceId == PlayedCharacterManager().id
            ):
                self._canMove = True
            return False

        if isinstance(msg, MapComplementaryInformationsDataMessage):
            self._mapHasAggressiveMonsters = msg.hasAggressiveMonsters
            return False

        else:
            return False

    def pulled(self) -> bool:
        return True

    def setNextMoveMapChange(self, mapId: float, autoTrip: bool = False) -> None:
        self._wantToChangeMap = mapId
        self._changeMapByAutoTrip = autoTrip

    def resetNextMoveMapChange(self) -> None:
        self._wantToChangeMap = -1
        self._changeMapByAutoTrip = False

    def setFollowingInteraction(self, interaction: object) -> None:
        self._followingIe = interaction

    def setFollowingMonsterFight(self, monsterGroup: object) -> None:
        self._followingMonsterGroup = monsterGroup

    def setFollowingMessage(self, message) -> None:
        if not isinstance(message, (INetworkMessage, Action)):
            raise Exception("The message is neither INetworkMessage or Action")
        self._followingMessage = message

    def forceNextMovementBehavior(self, pValue: int) -> None:
        self._nextMovementBehavior = pValue

    def askMoveTo(self, cell: MapPoint) -> bool:
        logger.debug(f"Asking to move to cell {cell}")
        if (
            not self._canMove
            or PlayedCharacterManager().state == PlayerLifeStatusEnum.STATUS_TOMBSTONE
        ):
            logger.debug("Can't move or dead, aborting")
            return False
        if self._isRequestingMovement:
            logger.debug("Already requesting movement, aborting")
            return False
        now: int = perf_counter()
        if self._latestMovementRequest + self.CONSECUTIVE_MOVEMENT_DELAY > now:
            logger.debug("Too soon to request movement, aborting")
            return False
        self._isRequestingMovement = True
        playerEntity: AnimatedCharacter = DofusEntities.getEntity(
            PlayedCharacterManager().id
        )
        if not playerEntity:
            logger.warn(
                "The player tried to move before its character was added to the scene. Aborting."
            )
            self._isRequestingMovement = False
            return False
        self._destinationPoint = cell.cellId
        if playerEntity.isMoving:
            playerEntity.stop()
            self._followingMove = cell
            logger.debug("Player is already moving, waiting for him to stop")
            return False
        movePath = Pathfinding.findPath(DataMapProvider(), playerEntity.position, cell)
        pathDuration = movePath.getCrossingDuration()
        # logger.info('Path estimated duration is : ' + str(pathDuration))
        self.sendPath(movePath)
        return True

    def sendPath(self, path: MovementPath) -> None:
        logger.info(f"Sending path {path}")
        originalPath: MovementPath = path.clone()
        if path.start.cellId == path.end.cellId:
            logger.warn(
                f"Discarding a movement path that begins and ends on the same cell ({path.start.cellId})."
            )
            self._isRequestingMovement = False
            if self._followingIe:
                self.activateSkill(
                    self._followingIe.skillInstanceId,
                    self._followingIe.ie,
                    self._followingIe.additionalParam,
                )
                self._followingIe = None
            if self._followingMonsterGroup:
                self.requestMonsterFight(self._followingMonsterGroup.id)
                self._followingMonsterGroup = None
            return
        forceWalk: bool = False
        gmmrmsg = GameMapMovementRequestMessage()
        keymoves = MapMovementAdapter.getServerMovement(path)
        gmmrmsg.init(keymoves, PlayedCharacterManager().currentMap.mapId)
        ConnectionsHandler.getConnection().send(gmmrmsg)
        logger.info(
            f"Sending a movement request to the server. Path length: {len(keymoves)}"
        )
        self._latestMovementRequest = perf_counter()

    def applyGameMapMovement(
        self, actorId: float, movement: MovementPath, forceWalking: bool = False
    ) -> None:
        movedEntity: IEntity = DofusEntities.getEntity(actorId)
        if movedEntity is None:
            logger.warn(
                f"The entity {actorId} moved before it was added to the scene. Aborting movement."
            )
            return
        self._lastMoveEndCellId = movement.end.cellId
        if movedEntity.id == PlayedCharacterManager().id:
            self._isRequestingMovement = False

    def askMapChange(self) -> None:
        logger.debug("Asking for a map change to map " + str(self._wantToChangeMap))
        cmmsg: ChangeMapMessage = ChangeMapMessage()
        cmmsg.init(self._wantToChangeMap, self._changeMapByAutoTrip)
        ConnectionsHandler.getConnection().send(cmmsg)

    def activateSkill(
        self, skillInstanceId: int, ie: InteractiveElement, additionalParam: int
    ) -> None:
        iurmsg: InteractiveUseRequestMessage = None
        iuwprmsg: InteractiveUseWithParamRequestMessage = None
        rpInteractivesFrame: RoleplayInteractivesFrame = (
            Kernel().getWorker().getFrame(RoleplayInteractivesFrame)
        )
        if (
            rpInteractivesFrame
            and rpInteractivesFrame.currentRequestedElementId != ie.elementId
            and not rpInteractivesFrame.usingInteractive
            and not rpInteractivesFrame.isElementChangingState(ie.elementId)
        ):
            rpInteractivesFrame.currentRequestedElementId = ie.elementId
            if additionalParam == 0:
                iurmsg = InteractiveUseRequestMessage()
                iurmsg.initInteractiveUseRequestMessage(ie.elementId, skillInstanceId)
                ConnectionsHandler.getConnection().send(iurmsg)
            else:
                iuwprmsg = InteractiveUseWithParamRequestMessage()
                iuwprmsg.initInteractiveUseWithParamRequestMessage(
                    ie.elementId, skillInstanceId, additionalParam
                )
                ConnectionsHandler.getConnection().send(iuwprmsg)
            self._canMove = False

    def requestMonsterFight(self, monsterGroupId: int) -> None:
        grpamrmsg: GameRolePlayAttackMonsterRequestMessage = (
            GameRolePlayAttackMonsterRequestMessage()
        )
        grpamrmsg.init(monsterGroupId)
        ConnectionsHandler.getConnection().send(grpamrmsg)

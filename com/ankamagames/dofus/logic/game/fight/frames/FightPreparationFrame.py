from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
from com.ankamagames.atouin.messages.CellClickMessage import CellClickMessage
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameContextKickAction import (
    GameContextKickAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameFightPlacementPositionRequestAction import (
    GameFightPlacementPositionRequestAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameFightPlacementSwapPositionsAcceptAction import (
    GameFightPlacementSwapPositionsAcceptAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameFightPlacementSwapPositionsCancelAction import (
    GameFightPlacementSwapPositionsCancelAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameFightPlacementSwapPositionsRequestAction import (
    GameFightPlacementSwapPositionsRequestAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.GameFightReadyAction import (
    GameFightReadyAction,
)
from com.ankamagames.dofus.logic.game.fight.actions.RemoveEntityAction import (
    RemoveEntityAction,
)
import com.ankamagames.dofus.logic.game.fight.frames.FightContextFrame as fightContextFrame
from com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame import (
    FightEntitiesFrame,
)
from com.ankamagames.dofus.logic.game.fight.types.SwapPositionRequest import (
    SwapPositionRequest,
)
from com.ankamagames.dofus.network.enums.TeamEnum import TeamEnum
from com.ankamagames.dofus.network.messages.game.context.GameContextDestroyMessage import (
    GameContextDestroyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextKickMessage import (
    GameContextKickMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntitiesDispositionMessage import (
    GameEntitiesDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntityDispositionErrorMessage import (
    GameEntityDispositionErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import (
    GameFightEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightLeaveMessage import (
    GameFightLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import (
    GameFightPlacementPositionRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPossiblePositionsMessage import (
    GameFightPlacementPossiblePositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsAcceptMessage import (
    GameFightPlacementSwapPositionsAcceptMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsCancelMessage import (
    GameFightPlacementSwapPositionsCancelMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsCancelledMessage import (
    GameFightPlacementSwapPositionsCancelledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsErrorMessage import (
    GameFightPlacementSwapPositionsErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsMessage import (
    GameFightPlacementSwapPositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsOfferMessage import (
    GameFightPlacementSwapPositionsOfferMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsRequestMessage import (
    GameFightPlacementSwapPositionsRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightReadyMessage import (
    GameFightReadyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightRemoveTeamMemberMessage import (
    GameFightRemoveTeamMemberMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightUpdateTeamMessage import (
    GameFightUpdateTeamMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolFightPreparationUpdateMessage import (
    IdolFightPreparationUpdateMessage,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.entities.messages.EntityClickMessage import (
    EntityClickMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint

logger = Logger(__name__)


class FightPreparationFrame(Frame):

    PLAYER_TEAM_ALPHA: float = 1

    ENEMY_TEAM_ALPHA: float = 0.3

    SELECTION_CHALLENGER: str = "FightPlacementChallengerTeam"

    SELECTION_DEFENDER: str = "FightPlacementDefenderTeam"

    _fightContextFrame: fightContextFrame.FightContextFrame

    _playerTeam: int

    _challengerPositions: list[int]

    _defenderPositions: list[int]

    _swapPositionRequests: list[SwapPositionRequest]

    _fightersId: list[float]

    def __init__(self, fightContextFrame: fightContextFrame.FightContextFrame):
        super().__init__()
        self._fightContextFrame = fightContextFrame

    @property
    def priority(self) -> int:
        return Priority.HIGH

    @property
    def fightersList(self) -> list[float]:
        return self._fightersId

    def pushed(self) -> bool:
        self._fightContextFrame.entitiesFrame.untargetableEntities = True
        DataMapProvider().isInFight = True
        self._swapPositionRequests = list[SwapPositionRequest](0)
        self._fightersId = list[float]()
        return True

    def updateSwapPositionRequestsIcons(self) -> None:
        swapPositionRequest = None
        for swapPositionRequest in self._swapPositionRequests:
            pass

    def setSwapPositionRequestsIconsVisibility(self, pVisible: bool) -> None:
        swapPositionRequest: SwapPositionRequest = None
        for swapPositionRequest in self._swapPositionRequests:
            pass

    def removeSwapPositionRequest(self, pRequestId: int) -> None:
        swapPositionRequest: SwapPositionRequest = None
        for swapPositionRequest in self._swapPositionRequests:
            if swapPositionRequest.requestId == pRequestId:
                del self._swapPositionRequests[
                    self._swapPositionRequests.index(swapPositionRequest)
                ]

    def isSwapPositionRequestValid(self, pRequestId: int) -> bool:
        swapPositionRequest: SwapPositionRequest = None
        for swapPositionRequest in self._swapPositionRequests:
            if swapPositionRequest.requestId == pRequestId:
                return True
        return False

    def process(self, msg: Message) -> bool:
        alreadyInTeam: bool = False
        indexOfCharToRemove: int = 0

        if isinstance(msg, GameFightLeaveMessage):
            gflmsg = msg
            if gflmsg.charId == PlayedCharacterManager().id:
                PlayedCharacterManager().fightId = -1
                Kernel().getWorker().removeFrame(self)
                gfemsg = GameFightEndMessage()
                gfemsg.init()
                fightContextFrame2 = Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
                if fightContextFrame2:
                    fightContextFrame2.process(gfemsg)
                else:
                    Kernel().getWorker().process(gfemsg)
                return True
            fighterSwapPositionRequests = self.getPlayerSwapPositionRequests(
                gflmsg.charId
            )
            for swapPositionRequest in fighterSwapPositionRequests:
                swapPositionRequest.destroy()
            return False

        if isinstance(msg, GameFightPlacementPossiblePositionsMessage):
            gfpppmsg = msg
            self._playerTeam = gfpppmsg.teamNumber
            return True

        if isinstance(msg, CellClickMessage):
            ccmsg = msg
            for entity in EntitiesManager().getEntitiesOnCell(ccmsg.cellId):
                if isinstance(entity, AnimatedCharacter) and not entity:
                    cellEntity = entity
            if cellEntity:
                fighter = object()
                fighter.name = self._fightContextFrame.getFighterName(cellEntity.id)
                entitiesFrame = Kernel().getWorker().getFrame(FightEntitiesFrame)
                fighterInfos = entitiesFrame.getEntityInfos(cellEntity.id)
                playerInfos = entitiesFrame.getEntityInfos(PlayedCharacterManager().id)
                if not (
                    fighterInfos.contextualId != playerInfos.contextualId
                    and fighterInfos.spawnInfo.teamId == playerInfos.spawnInfo.teamId
                ):
                    return True
            elif (
                self.isValidPlacementCell(ccmsg.cellId, self._playerTeam)
                and not self._fightContextFrame.onlyTheOtherTeamCanPlace
            ):
                gfpprmsg = GameFightPlacementPositionRequestMessage()
                gfpprmsg.init(ccmsg.cellId)
                ConnectionsHandler.getConnection().send(gfpprmsg)
            return True

        if isinstance(msg, GameFightPlacementPositionRequestAction):
            gfppra = msg
            if not self._fightContextFrame.onlyTheOtherTeamCanPlace:
                gfpprmsg2 = GameFightPlacementPositionRequestMessage()
                gfpprmsg2.init(gfppra.cellId)
                ConnectionsHandler.getConnection().send(gfpprmsg2)
            return True

        if isinstance(msg, GameEntitiesDispositionMessage) or isinstance(
            msg, GameFightPlacementSwapPositionsMessage
        ):
            for iedi in msg["dispositions"]:
                entitySwapPositionsRequests = self.getPlayerSwapPositionRequests(
                    iedi.id
                )
                for swapPositionRequest in entitySwapPositionsRequests:
                    swapPositionRequest.destroy()
            return False

        if isinstance(msg, GameFightPlacementSwapPositionsRequestAction):
            gfpspra = msg
            gfpsprmsg = GameFightPlacementSwapPositionsRequestMessage()
            gfpsprmsg.init(gfpspra.requestedId, gfpspra.cellId)
            ConnectionsHandler.getConnection().send(gfpsprmsg)
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsOfferMessage):
            gfpspomsg = msg
            entitiesFrame = Kernel().getWorker().getFrame(FightEntitiesFrame)
            swapPositionRequest = SwapPositionRequest(
                gfpspomsg.requestId, gfpspomsg.requesterId, gfpspomsg.requestedId
            )
            if swapPositionRequest.requestedId == PlayedCharacterManager().id:
                self._swapPositionRequests.append(swapPositionRequest)
            elif swapPositionRequest.requesterId == PlayedCharacterManager().id:
                self._swapPositionRequests.append(swapPositionRequest)
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsErrorMessage):
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsAcceptAction):
            gfpspaa = msg
            gfpspamsg = GameFightPlacementSwapPositionsAcceptMessage()
            gfpspamsg.init(gfpspaa.requestId)
            ConnectionsHandler.getConnection().send(gfpspamsg)
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsCancelAction):
            gfpspca = msg
            gfpspcmsg = GameFightPlacementSwapPositionsCancelMessage()
            gfpspcmsg.init(gfpspca.requestId)
            ConnectionsHandler.getConnection().send(gfpspcmsg)
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsCancelledMessage):
            gfpspcdmsg = msg
            swapPositionRequest = self.getSwapPositionRequest(gfpspcdmsg.requestId)
            if swapPositionRequest:
                swapPositionRequest.destroy()
                if (
                    swapPositionRequest.requesterId == PlayedCharacterManager().id
                    and gfpspcdmsg.cancellerId != PlayedCharacterManager().id
                ):
                    entitiesFrame = Kernel().getWorker().getFrame(FightEntitiesFrame)
                    cancellerInfo = entitiesFrame.getEntityInfos(gfpspcdmsg.cancellerId)
            return True

        if isinstance(msg, GameEntityDispositionErrorMessage):
            logger.error("Cette position n'est pas accessible.")
            return True

        if isinstance(msg, GameFightReadyAction):
            gfra = msg
            gfrmsg = GameFightReadyMessage()
            gfrmsg.init(gfra.isReady)
            ConnectionsHandler.getConnection().send(gfrmsg)
            return True

        if isinstance(msg, EntityClickMessage):
            ecmsg = msg
            clickedEntity = ecmsg.entity
            if clickedEntity:
                entitiesFrame = Kernel().getWorker().getFrame(FightEntitiesFrame)
                fighterInfos = entitiesFrame.getEntityInfos(clickedEntity.id)
                playerInfos = entitiesFrame.getEntityInfos(PlayedCharacterManager().id)
                if not (
                    fighterInfos
                    and playerInfos
                    and fighterInfos.contextualId != playerInfos.contextualId
                    and fighterInfos.spawnInfo.teamId == playerInfos.spawnInfo.teamId
                ):
                    return True
            return True

        if isinstance(msg, GameContextKickAction):
            gcka = msg
            gckmsg = GameContextKickMessage()
            gckmsg.init(gcka.targetId)
            ConnectionsHandler.getConnection().send(gckmsg)
            return True

        if isinstance(msg, GameFightUpdateTeamMessage):
            gfutmsg = msg
            gfutmsg_myId = PlayedCharacterManager().id
            alreadyInTeam = False
            for teamMember in gfutmsg.team.teamMembers:
                if teamMember.id == gfutmsg_myId:
                    alreadyInTeam = True
                if self._fightersId.find(teamMember.id) == -1:
                    self._fightersId.append(teamMember.id)
            if (
                alreadyInTeam
                or len(gfutmsg.team.teamMembers) >= 1
                and gfutmsg.team.teamMembers[0].id == gfutmsg_myId
            ):
                PlayedCharacterManager().teamId = gfutmsg.team.teamId
                self._fightContextFrame.isFightLeader = (
                    gfutmsg.team.leaderId == gfutmsg_myId
                )
            return True

        if isinstance(msg, GameFightRemoveTeamMemberMessage):
            gfrtmmsg = msg
            self._fightContextFrame.entitiesFrame.process(
                RemoveEntityAction.create(gfrtmmsg.charId)
            )
            indexOfCharToRemove = self._fightersId.find(gfrtmmsg.charId)
            if indexOfCharToRemove != -1:
                self._fightersId.splice(indexOfCharToRemove, 1)
            return True

        if isinstance(msg, GameContextDestroyMessage):
            gfemsg2 = GameFightEndMessage()
            gfemsg2.initGameFightEndMessage()
            fightContextFrame = Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
            if fightContextFrame:
                fightContextFrame.process(gfemsg2)
            else:
                Kernel().getWorker().process(gfemsg2)
            return True

        if isinstance(msg, IdolFightPreparationUpdateMessage):
            return True

        else:
            return False

    def pulled(self) -> bool:
        swapPositionRequest: SwapPositionRequest = None
        DataMapProvider().isInFight = False
        self.removeSelections()
        for swapPositionRequest in self._swapPositionRequests:
            swapPositionRequest.destroy()
        return True

    def removeSelections(self) -> None:
        sc: Selection = SelectionManager().getSelection(self.SELECTION_CHALLENGER)
        if sc:
            sc.remove()
        sd: Selection = SelectionManager().getSelection(self.SELECTION_DEFENDER)
        if sd:
            sd.remove()

    def isValidPlacementCell(self, cellId: int, team: int) -> bool:
        mapPoint: MapPoint = MapPoint.fromCellId(cellId)
        if not DataMapProvider().pointMov(mapPoint.x, mapPoint.y, False):
            return False
        validCells: list[int] = list[int]()
        if team == TeamEnum.TEAM_CHALLENGER:
            validCells = self._challengerPositions
        if team == TeamEnum.TEAM_DEFENDER:
            validCells = self._defenderPositions
        if team == TeamEnum.TEAM_SPECTATOR:
            return False
        if validCells:
            for vc in validCells:
                if vc == cellId:
                    return True
        return False

    def getSwapPositionRequest(self, pRequestId: int) -> SwapPositionRequest:
        swapPositionRequest: SwapPositionRequest = None
        for swapPositionRequest in self._swapPositionRequests:
            if swapPositionRequest.requestId == pRequestId:
                return swapPositionRequest
        return None

    def getPlayerSwapPositionRequests(
        self, pPlayerId: float
    ) -> list[SwapPositionRequest]:
        swapPositionRequest: SwapPositionRequest = None
        swapPositionRequests: list[SwapPositionRequest] = list[SwapPositionRequest](0)
        for swapPositionRequest in self._swapPositionRequests:
            if (
                swapPositionRequest.requesterId == pPlayerId
                or swapPositionRequest.requestedId == pPlayerId
            ):
                swapPositionRequests.append(swapPositionRequest)
        return swapPositionRequests

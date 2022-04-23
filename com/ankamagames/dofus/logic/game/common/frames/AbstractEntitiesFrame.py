from abc import abstractmethod
from com.ankamagames.dofus.datacenter.monsters.Monster import Monster
from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import (
    WorldPointWrapper,
)
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
import com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager as pcm
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import (
    EntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import (
    GameContextActorInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import (
    GameFightMonsterInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import (
    GameRolePlayHumanoidInformations,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import (
    InteractiveElement,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint

logger = Logger(__name__)


class AbstractEntitiesFrame(Frame):
    def __init__(self):
        self._entities = dict()

        self._entitiesTotal: int = 0

        self._creaturesMode: bool = False

        self._creaturesLimit: int = -1

        self._entitiesVisibleNumber: int = 0

        self._untargetableEntities: bool = False

        self._interactiveElements = list[InteractiveElement]()

        self._currentSubAreaId: int = None

        self._worldPoint: WorldPointWrapper = None

        self._creaturesFightMode: bool = False

        self._justSwitchingCreaturesFightMode: bool = False

        self._entitiesIconsCounts = dict()

        self._entitiesIconsNames = dict()

        self._entitiesIcons = dict()

        self._entitiesIconsOffsets = dict()

        self._carriedEntities = dict()

        self._pendingCarriedEntities = dict()

        self._updateAllIcons: bool = None

        self._showIcons: bool = True

        self._isShowIconsChanged: bool = False

        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    def pushed(self) -> bool:
        self._entities = dict()
        self._entitiesTotal = 0
        return True

    @abstractmethod
    def process(msg: Message) -> bool:
        pass

    def getEntityInfos(self, entityId: float) -> GameContextActorInformations:
        if entityId == 0 or entityId is None:
            return None
        if not self._entities or not self._entitiesTotal:
            return None
        if not self._entities.get(entityId):
            if entityId <= EntitiesManager.RANDOM_ENTITIES_ID_START:
                return None
            logger.error(f"Entity {entityId} is unknown.")
            return None
        return self._entities.get(entityId)

    def getEntitiesIdsList(self) -> list[float]:
        gcai: GameContextActorInformations = None
        entitiesList: list[float] = list[float](0, False)
        for gcai in self._entities:
            entitiesList.append(gcai.contextualId)
        return entitiesList

    def hasEntity(self, entityId: float) -> bool:
        return (
            self._entities is not None
            and self._entitiesTotal > 0
            and entityId in self._entities
        )

    def registerActor(self, infos: GameContextActorInformations) -> None:
        self.registerActorWithId(infos, infos.contextualId)

    def registerActorWithId(
        self, infos: GameContextActorInformations, actorId: float
    ) -> None:
        if self._entities == None:
            self._entities = dict()
        if not self._entities.get(actorId):
            self._entitiesTotal += 1
        self._entities[actorId] = infos
        if isinstance(infos, GameFightFighterInformations):
            StatsManager().addRawStats(actorId, infos)

    def unregisterActor(self, actorId: float) -> None:
        entity: IEntity = None
        if self._entities[actorId]:
            entity = DofusEntities.getEntity(actorId)
            if entity != None and isinstance(entity, AnimatedCharacter):
                entity
            self._entitiesTotal -= 1
        del self._entities[actorId]
        StatsManager().deleteStats(actorId)

    def addOrUpdateActor(
        self, infos: GameContextActorInformations
    ) -> AnimatedCharacter:
        characterEntity: AnimatedCharacter = DofusEntities.getEntity(infos.contextualId)
        self.registerActor(infos)
        if isinstance(infos, GameFightFighterInformations):
            StatsManager().addRawStats(infos.contextualId, infos)
        if characterEntity is None:
            characterEntity = AnimatedCharacter(infos.contextualId)
            if isinstance(infos, GameFightMonsterInformations):
                characterEntity.speedAdjust = Monster.getMonsterById(
                    GameFightMonsterInformations(infos).creatureGenericId
                ).speedAdjust
            EntitiesManager().addAnimatedEntity(
                int(infos.contextualId), characterEntity
            )
        if isinstance(infos, GameRolePlayHumanoidInformations):
            humanoid = infos
            if infos.contextualId == pcm.PlayedCharacterManager().id:
                pcm.PlayedCharacterManager().restrictions = (
                    humanoid.humanoidInfo.restrictions
                )
        if infos.disposition.cellId != -1:
            characterEntity.position = MapPoint.fromCellId(infos.disposition.cellId)
        return characterEntity

    def updateActorDisposition(
        self, actorId: float, newDisposition: EntityDispositionInformations
    ) -> None:
        if self._entities.get(actorId):
            self._entities[actorId].disposition = newDisposition
        else:
            logger.warn(
                f"Cannot update unknown actor disposition ({actorId}) in informations."
            )

    def removeActor(self, actorId: float) -> None:
        self.unregisterActor(actorId)

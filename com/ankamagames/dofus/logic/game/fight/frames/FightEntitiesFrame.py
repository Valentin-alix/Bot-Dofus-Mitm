from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import (
    WorldPointWrapper,
)
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.frames.AbstractEntitiesFrame import (
    AbstractEntitiesFrame,
)
import com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager as pcm
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.fight.actions.RemoveEntityAction import (
    RemoveEntityAction,
)
import com.ankamagames.dofus.logic.game.fight.fightEvents.FightEventsHelper as fightEventsHelper
import com.ankamagames.dofus.logic.game.fight.frames.FightBattleFrame as fightBattleFrame
import com.ankamagames.dofus.logic.game.fight.frames.FightPreparationFrame as fightPreparationFrame
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
    CurrentPlayedFighterManager,
)
from com.ankamagames.dofus.network.enums.GameActionFightInvisibilityStateEnum import (
    GameActionFightInvisibilityStateEnum,
)
from com.ankamagames.dofus.network.enums.MapObstacleStateEnum import (
    MapObstacleStateEnum,
)
from com.ankamagames.dofus.network.enums.TeamEnum import TeamEnum
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightCarryCharacterMessage import (
    GameActionFightCarryCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDropCharacterMessage import (
    GameActionFightDropCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightThrowCharacterMessage import (
    GameActionFightThrowCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.character.status.PlayerStatusUpdateMessage import (
    PlayerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRefreshEntityLookMessage import (
    GameContextRefreshEntityLookMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntitiesDispositionMessage import (
    GameEntitiesDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntityDispositionMessage import (
    GameEntityDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import (
    ShowCellMessage,
)
from com.ankamagames.dofus.network.messages.game.context.ShowCellSpectatorMessage import (
    ShowCellSpectatorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightHumanReadyStateMessage import (
    GameFightHumanReadyStateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsMessage import (
    GameFightPlacementSwapPositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightRefreshFighterMessage import (
    GameFightRefreshFighterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import (
    GameFightShowFighterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterRandomStaticPoseMessage import (
    GameFightShowFighterRandomStaticPoseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataInHouseMessage import (
    MapComplementaryInformationsDataInHouseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import (
    MapComplementaryInformationsDataMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsWithCoordsMessage import (
    MapComplementaryInformationsWithCoordsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRewardRateMessage import (
    MapRewardRateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.anomaly.AnomalyStateMessage import (
    AnomalyStateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.MapComplementaryInformationsBreachMessage import (
    MapComplementaryInformationsBreachMessage,
)
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import (
    EntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.FightEntityDispositionInformations import (
    FightEntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import (
    GameContextActorInformations,
)
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import (
    GameContextActorPositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import (
    IdentifiedEntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacterInformations import (
    GameFightCharacterInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEntityInformation import (
    GameFightEntityInformation,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import (
    GameFightFighterNamedInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import (
    GameFightMonsterInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import (
    BreachBranch,
)
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import (
    InteractiveElement,
)
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import (
    StatedElement,
)
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.events.PropertyChangeEvent import PropertyChangeEvent
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from damageCalculation.tools.StatIds import StatIds

logger = Logger(__name__)


class FightEntitiesFrame(AbstractEntitiesFrame, Frame):

    TEAM_CIRCLE_COLOR_1: int = 255

    TEAM_CIRCLE_COLOR_2: int = 16711680

    _ie: dict

    _tempFighterList: list

    _illusionEntities: dict

    _entitiesNumber: dict

    _lastKnownPosition: dict

    _lastKnownMovementPoint: dict

    _lastKnownPlayerStatus: dict

    _realFightersLooks: dict

    _mountsVisible: bool

    _numCreatureSwitchingEntities: int

    _entitiesIconsToUpdate: list[float]

    lastKilledChallengers: list[GameFightFighterInformations]

    lastKilledDefenders: list[GameFightFighterInformations]

    def __init__(self):
        self._ie = dict(True)
        self._tempFighterList = []
        self._entitiesIconsToUpdate = list[float](0)
        self.lastKilledChallengers = list[GameFightFighterInformations](0)
        self.lastKilledDefenders = list[GameFightFighterInformations](0)
        super().__init__()

    def getCurrentInstance(self) -> "FightEntitiesFrame":
        return krnl.Kernel().getWorker().getFrame(FightEntitiesFrame)

    def pushed(self) -> bool:
        self._entitiesNumber = dict()
        self._illusionEntities = dict()
        self._lastKnownPosition = dict()
        self._lastKnownMovementPoint = dict()
        self._lastKnownPlayerStatus = dict()
        self._realFightersLooks = dict()
        return super().pushed()

    def addLastKilledAlly(self, entity: GameFightFighterInformations) -> None:
        listKilled: list[GameFightFighterInformations] = (
            self.lastKilledChallengers
            if entity.spawnInfo.teamId == TeamEnum.TEAM_CHALLENGER
            else self.lastKilledDefenders
        )
        index: int = 0
        if not isinstance(entity, GameFightFighterNamedInformations):
            while index < len(listKilled) and isinstance(
                listKilled[index], GameFightFighterNamedInformations
            ):
                index += 1
            if not isinstance(entity, GameFightEntityInformation):
                while index < len(listKilled) and isinstance(
                    listKilled[index] is GameFightEntityInformation
                ):
                    index += 1
        if entity.spawnInfo.teamId == TeamEnum.TEAM_CHALLENGER:
            self.lastKilledChallengers.insert(index, entity)
        else:
            self.lastKilledDefenders.insert(index, entity)

    def removeSpecificKilledAlly(self, infos: GameFightFighterInformations) -> None:
        if (
            infos.spawnInfo.teamId == TeamEnum.TEAM_CHALLENGER
            and len(self.lastKilledChallengers) > 0
        ):
            self.lastKilledChallengers.pop(self.lastKilledChallengers.index(infos))
        elif (
            infos.spawnInfo.teamId == TeamEnum.TEAM_DEFENDER
            and len(self.lastKilledDefenders) > 0
        ):
            self.lastKilledDefenders.pop(self.lastKilledDefenders.index(infos))

    def removeLastKilledAlly(self, teamId: int) -> None:
        if teamId == TeamEnum.TEAM_CHALLENGER and len(self.lastKilledChallengers) > 0:
            self.lastKilledChallengers.pop(0)
        elif teamId == TeamEnum.TEAM_DEFENDER and len(self.lastKilledDefenders) > 0:
            self.lastKilledDefenders.pop(0)

    def addOrUpdateActor(
        self, infos: GameContextActorInformations
    ) -> AnimatedCharacter:
        res = super().addOrUpdateActor(infos)
        if infos.disposition.cellId != -1:
            self.setLastKnownEntityPosition(
                infos.contextualId, infos.disposition.cellId
            )
        if infos.contextualId > 0:
            pass
        if CurrentPlayedFighterManager().currentFighterId == infos.contextualId:
            res.canSeeThrough = True
        if isinstance(infos, GameFightCharacterInformations):
            self._lastKnownPlayerStatus[infos.contextualId] = infos.status.statusId
        return res

    def process(self, msg: Message) -> bool:

        if isinstance(msg, GameFightRefreshFighterMessage):
            gfrfmsg = msg
            actorId = gfrfmsg.informations.contextualId
            fullInfos = self._entities.get(actorId)
            if fullInfos != None:
                fullInfos.disposition = gfrfmsg.informations.disposition
                fullInfos.look = gfrfmsg.informations.look
                self._realFightersLooks[
                    gfrfmsg.informations.contextualId
                ] = gfrfmsg.informations.look
                if (
                    krnl.Kernel().getWorker().contains(fightPreparationFrame.FightPreparationFrame)
                    and gfrfmsg.informations.disposition.cellId == -1
                ):
                    self.registerActor(gfrfmsg.informations)
                else:
                    self.updateActor(fullInfos, True)
            if krnl.Kernel().getWorker().getFrame(fightPreparationFrame.FightPreparationFrame):
                pass
            return True

        if isinstance(msg, GameFightShowFighterMessage):
            gfsfmsg = msg
            self._realFightersLooks[
                gfsfmsg.informations.contextualId
            ] = gfsfmsg.informations.look
            if isinstance(msg, GameFightShowFighterRandomStaticPoseMessage):
                self.updateFighter(gfsfmsg.informations)
                self._illusionEntities[gfsfmsg.informations.contextualId] = True
            else:
                if (
                    krnl.Kernel().getWorker().contains(fightPreparationFrame.FightPreparationFrame)
                    and gfsfmsg.informations.disposition.cellId == -1
                ):
                    self.registerActor(gfsfmsg.informations)
                else:
                    self.updateFighter(gfsfmsg.informations)
                self._illusionEntities[gfsfmsg.informations.contextualId] = False
            fightContextFrame = (
                krnl.Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
            )
            if fightContextFrame.fightersPositionsHistory[
                gfsfmsg.informations.contextualId
            ]:
                pass
            return True

        if isinstance(msg, GameFightHumanReadyStateMessage):
            gfhrsmsg = msg
            fighterInfoToBeReady = self.getEntityInfos(gfhrsmsg.characterId)
            if (
                not fighterInfoToBeReady
                or fighterInfoToBeReady.disposition.cellId == -1
            ):
                return True
            ac2 = self.addOrUpdateActor(fighterInfoToBeReady)
            if gfhrsmsg.isReady:
                pass
            else:
                if gfhrsmsg.characterId == pcm.PlayedCharacterManager().id:
                    pass
            fightPreparationFrame = (
                krnl.Kernel().getWorker().getFrame(fightPreparationFrame.FightPreparationFrame)
            )
            if fightPreparationFrame:
                pass
            return True

        if isinstance(msg, GameEntityDispositionMessage):
            gedmsg = msg
            if gedmsg.disposition.id == CurrentPlayedFighterManager().currentFighterId:
                pass
            self.updateActorDisposition(gedmsg.disposition.id, gedmsg.disposition)
            return True

        if isinstance(msg, GameFightPlacementSwapPositionsMessage):
            gfpspmsg = msg
            for iedi in gfpspmsg.dispositions:
                self.updateActorDisposition(iedi.id, iedi)
            return True

        if isinstance(msg, GameEntitiesDispositionMessage):
            gedsmsg = msg
            for disposition in gedsmsg.dispositions:
                fighterInfos = self.getEntityInfos(disposition.id)
                if (
                    fighterInfos
                    and fighterInfos.stats.invisibilityState
                    != GameActionFightInvisibilityStateEnum.INVISIBLE
                ):
                    self.updateActorDisposition(disposition.id, disposition)
            return True

        if isinstance(msg, GameContextRefreshEntityLookMessage):
            return True

        if isinstance(msg, RemoveEntityAction):
            fighterRemovedId = msg.actorId
            self._entitiesNumber[fighterRemovedId] = None
            self.removeActor(fighterRemovedId)
            del self._realFightersLooks[fighterRemovedId]
            return True

        if isinstance(msg, ShowCellSpectatorMessage):
            return True

        if isinstance(msg, ShowCellMessage):
            return True

        if isinstance(msg, MapComplementaryInformationsDataMessage):
            mcidmsg = msg
            self._interactiveElements = mcidmsg.interactiveElements
            if isinstance(msg, MapComplementaryInformationsWithCoordsMessage):
                mciwcmsg = msg
                if pcm.PlayedCharacterManager().isInHouse:
                    pass
                pcm.PlayedCharacterManager().isInHouse = False
                pcm.PlayedCharacterManager().isInHisHouse = False
                pcm.PlayedCharacterManager().currentMap.setOutdoorCoords(
                    mciwcmsg.worldX, mciwcmsg.worldY
                )
                self._worldPoint = WorldPointWrapper(
                    mciwcmsg.mapId, True, mciwcmsg.worldX, mciwcmsg.worldY
                )

            elif isinstance(msg, MapComplementaryInformationsDataInHouseMessage):
                mcidihmsg = msg
                isPlayerHouse = (
                    PlayerManager().nickname
                    == mcidihmsg.currentHouse.houseInfos.ownerTag.nickname
                )
                pcm.PlayedCharacterManager().isInHouse = True
                if isPlayerHouse:
                    pcm.PlayedCharacterManager().isInHisHouse = True
                pcm.PlayedCharacterManager().currentMap.setOutdoorCoords(
                    mcidihmsg.currentHouse.worldX, mcidihmsg.currentHouse.worldY
                )
                self._worldPoint = WorldPointWrapper(
                    mcidihmsg.mapId,
                    True,
                    mcidihmsg.currentHouse.worldX,
                    mcidihmsg.currentHouse.worldY,
                )

            elif isinstance(msg, MapComplementaryInformationsBreachMessage):
                return True

        if isinstance(msg, AnomalyStateMessage):
            taimsg = msg
            return True

        if isinstance(msg, MapRewardRateMessage):
            mrrmsg = msg
            return True

        if isinstance(msg, GameActionFightCarryCharacterMessage):
            gafccmsg = msg
            if gafccmsg.cellId != -1:
                for ent in self._entities:
                    if ent.contextualId == gafccmsg.targetId:
                        ent.disposition.carryingCharacterId = gafccmsg.sourceId
                        self._tempFighterList.append(
                            TmpFighterInfos(ent.contextualId, gafccmsg.sourceId)
                        )
            return True

        if isinstance(msg, GameActionFightThrowCharacterMessage):
            gaftcmsg = msg
            self.dropEntity(gaftcmsg.targetId)
            return True

        if isinstance(msg, GameActionFightDropCharacterMessage):
            gafdcmsg = msg
            self.dropEntity(gafdcmsg.targetId)
            return True

        if isinstance(msg, PlayerStatusUpdateMessage):
            psum = msg
            self._lastKnownPlayerStatus[psum.playerId] = psum.status.statusId
            return False

        else:
            return False

    def dropEntity(self, targetId: float) -> None:
        index: int = 0
        ent: GameFightFighterInformations = None
        for ent in self._entities:
            if ent.contextualId == targetId:
                ent.disposition.carryingCharacterId = None
                index = self.getTmpFighterInfoIndex(ent.contextualId)
                if (
                    self._tempFighterList != None
                    and len(self._tempFighterList) != 0
                    and index != -1
                ):
                    self._tempFighterList.splice(index, 1)
                return

    def showCreaturesInFight(self, activated: bool = False) -> None:
        self._creaturesFightMode = activated
        self._justSwitchingCreaturesFightMode = True
        self._numCreatureSwitchingEntities = 0
        for ent in self._entities.values():
            self.updateFighter(ent)
        self._justSwitchingCreaturesFightMode = False
        if self._numCreatureSwitchingEntities == 0:
            self.onCreatureSwitchEnd(None)

    def entityIsIllusion(self, id: float) -> bool:
        return self._illusionEntities[id]

    def getLastKnownEntityPosition(self, id: float) -> int:
        return (
            self._lastKnownPosition[id] != int(self._lastKnownPosition[id])
            if None
            else -1
        )

    def setLastKnownEntityPosition(self, id: float, value: int) -> None:
        self._lastKnownPosition[id] = value

    def getLastKnownEntityMovementPoint(self, id: float) -> int:
        return (
            self._lastKnownMovementPoint[id] != int(self._lastKnownMovementPoint[id])
            if None
            else 0
        )

    def setLastKnownEntityMovementPoint(
        self, id: float, value: int, add: bool = False
    ) -> None:
        if self._lastKnownMovementPoint[id] == None:
            self._lastKnownMovementPoint[id] = 0
        if not add:
            self._lastKnownMovementPoint[id] = value
        else:
            self._lastKnownMovementPoint[id] += value

    def pulled(self) -> bool:
        self._tempFighterList = None
        for obj in self._ie:
            self.removeInteractive(obj.element)
        for fighterId in self._realFightersLooks:
            del self._realFightersLooks[fighterId]
        return super().pulled()

    def registerInteractive(self, ie: InteractiveElement, firstSkill: int) -> None:
        s = None
        cie: InteractiveElement = None
        worldObject: InteractiveObject = Atouin().getIdentifiedElement(ie.elementId)
        if not worldObject:
            logger.error(
                "Unknown identified element "
                + ie.elementId
                + ", unable to register it as interactive."
            )
            return
        found: bool = False
        for s in interactiveElements:
            cie = interactiveElements[int(s)]
            if cie.elementId == ie.elementId:
                found = True
                interactiveElements[int(s)] = ie
        if not found:
            interactiveElements.append(ie)
        worldPos: MapPoint = Atouin().getIdentifiedElementPosition(ie.elementId)
        self._ie[worldObject] = {
            "element": ie,
            "position": worldPos,
            "firstSkill": firstSkill,
        }

    def updateStatedElement(self, se: StatedElement) -> None:
        worldObject: InteractiveObject = Atouin().getIdentifiedElement(se.elementId)
        if not worldObject:
            logger.error(
                "Unknown identified element "
                + se.elementId
                + " unable to change its state to "
                + se.elementState
                + " !"
            )
            return
        ts: TiphonSprite = (
            self.findTiphonSpriteworldObject
            if isinstance(worldObject, DisplayObjectContainer)
            else None
        )
        if not ts:
            logger.warn(
                "Unable to find an animated element for the stated element "
                + se.elementId
                + " on cell "
                + se.elementCellId
                + ", self element is probably invisible or is not configured as an animated element."
            )
            return
        ts.setAnimationAndDirection("AnimState1", 0)

    def removeInteractive(self, ie: InteractiveElement) -> None:
        interactiveElement: InteractiveObject = Atouin().getIdentifiedElement(
            ie.elementId
        )
        del self._ie[interactiveElement]

    # def onCreatureSwitchEnd(self, pEvent: TiphonEvent) -> None:
    #     if pEvent:
    #         pEvent.currentTarget.removeEventListener(
    #             TiphonEvent.RENDER_SUCCEED, self.onCreatureSwitchEnd
    #         )
    #         --self._numCreatureSwitchingEntities
    #     if self._numCreatureSwitchingEntities == 0:
    #         fightPreparationFrame = (
    #             krnl.Kernel().getWorker().getFrame(fightPreparationFrame.FightPreparationFrame)
    #         )
    #         if fightPreparationFrame:
    #             fightPreparationFrame.updateSwapPositionRequestsIcons()

    def getOrdonnedPreFighters(self) -> list[float]:
        entitiesIds: list[float] = self.getEntitiesIdsList()
        fighters: list[float] = list[float]()
        if not entitiesIds or len(entitiesIds) <= 1:
            return fighters
        goodGuys: list = []
        badGuys: list = []
        hiddenGuys: list = []
        badInit: int = 0
        goodInit: int = 0
        for id in entitiesIds:
            entityInfo = self.getEntityInfos(id)
            if entityInfo:
                if (
                    isinstance(entityInfo, GameFightFighterNamedInformations)
                    and entityInfo
                ):
                    hiddenGuys.append(id)
                else:
                    stats = StatsManager().getStats(entityInfo.contextualId)
                    monsterGenericId = 0
                    if isinstance(entityInfo, GameFightMonsterInformations):
                        monsterGenericId = entityInfo.creatureGenericId
                    if stats:
                        initiative = stats.getStatTotalValue(StatIds.INITIATIVE)
                        lifePoints = stats.getHealthPoints()
                        maxLifePoints = stats.getMaxHealthPoints()
                        if entityInfo.spawnInfo.teamId == 0:
                            badGuys.push(
                                {
                                    "fighterId": id,
                                    "init": initiative * lifePoints / maxLifePoints,
                                    "monsterId": monsterGenericId,
                                }
                            )
                            badInit += initiative * lifePoints / maxLifePoints
                        else:
                            badGuys.push(
                                {
                                    "fighterId": id,
                                    "init": initiative * lifePoints / maxLifePoints,
                                    "monsterId": monsterGenericId,
                                }
                            )
                            goodInit += initiative * lifePoints / maxLifePoints
        badGuys.sortOn(
            ["init", "monsterId", "fighterId"], list.DESCENDING | list.NUMERIC
        )
        goodGuys.sortOn(
            ["init", "monsterId", "fighterId"], list.DESCENDING | list.NUMERIC
        )
        badStart = True
        if (
            len(badGuys) == 0
            or len(goodGuys) == 0
            or badInit / len(badGuys) < goodInit / len(goodGuys)
        ):
            badStart = False
        length: int = max(len(badGuys), len(goodGuys))
        for i in range(length):
            if badStart:
                if badGuys[i]:
                    fighters.append(badGuys[i].fighterId)
                if goodGuys[i]:
                    fighters.append(goodGuys[i].fighterId)
            else:
                if goodGuys[i]:
                    fighters.append(goodGuys[i].fighterId)
                if badGuys[i]:
                    fighters.append(badGuys[i].fighterId)
        for e in hiddenGuys.reverse():
            fighters = fighters.insert(0, e)
        return fighters

    def removeSwords(self) -> None:
        entInfo = None
        ac: AnimatedCharacter = None
        for entInfo in self._entities:
            if not (
                isinstance(entInfo, GameFightCharacterInformations)
                and not GameFightCharacterInformations(entInfo).spawnInfo.alive
            ):
                ac = self.addOrUpdateActor(entInfo)
                ac.removeBackground("readySwords")

    def updateFighter(self, fighterInfos: GameFightFighterInformations) -> None:
        lastInvisibilityStat: int = 0
        fighterId: float = fighterInfos.contextualId
        if fighterInfos.spawnInfo.alive:
            lastInvisibilityStat = -1
            lastFighterInfo = self._entities[fighterId]
            if lastFighterInfo:
                lastInvisibilityStat = lastFighterInfo.stats.invisibilityState
            ac = self.addOrUpdateActor(fighterInfos)
            if (
                lastInvisibilityStat == GameActionFightInvisibilityStateEnum.INVISIBLE
                and fighterInfos.stats.invisibilityState == lastInvisibilityStat
            ):
                self.registerActor(fighterInfos)
                return
            if lastFighterInfo != fighterInfos:
                if fighterId == CurrentPlayedFighterManager().currentFighterId:
                    pass
            if (
                fighterInfos.stats.invisibilityState
                != GameActionFightInvisibilityStateEnum.VISIBLE
                and fighterInfos.stats.invisibilityState != lastInvisibilityStat
            ):
                pass
        else:
            self.updateActor(fighterInfos, False)
        self.updateCarriedEntities(fighterInfos)

    def isEntityAlive(self, entityId: float) -> bool:
        if not self.hasEntity(entityId):
            return False
        entityInfo: GameContextActorInformations = self.getEntityInfos(entityId)
        return (
            isinstance(entityInfo, GameFightFighterInformations)
            and entityInfo.spawnInfo.alive
        )

    def updateActor(
        self, actorInfos: GameContextActorInformations, alive: bool = True
    ) -> None:
        if alive:
            self.addOrUpdateActor(actorInfos)
        else:
            if self._entities[actorInfos.contextualId]:
                self.hideActor(actorInfos.contextualId)
            self.registerActor(actorInfos)

    def updateActorLook(
        self, actorId: float, newLook: EntityLook, smoke: bool = False
    ) -> AnimatedCharacter:
        ac: AnimatedCharacter = super().updateActorLook(actorId, newLook, smoke)
        if ac and actorId != pcm.PlayedCharacterManager().id:
            pass
        return ac

    def updateCarriedEntities(self, fighterInfos: GameContextActorInformations) -> None:
        hasCarryingModifier: bool = False
        fighterId: float = fighterInfos.contextualId
        num: int = len(self._tempFighterList)
        i: int = 0
        while i < num:
            infos = self._tempFighterList[i]
            carryingCharacterId = infos.carryingCharacterId
            if fighterId == carryingCharacterId:
                del self._tempFighterList[i]
                self.startCarryStep(carryingCharacterId, infos.contextualId)
            i += 1
        if isinstance(fighterInfos.disposition, FightEntityDispositionInformations):
            fedi = fighterInfos.disposition
            if fedi.carryingCharacterId:
                carryingEntity = DofusEntities.getEntity(fedi.carryingCharacterId)
                if not carryingEntity:
                    self._tempFighterList.append(
                        TmpFighterInfos(
                            fighterInfos.contextualId, fedi.carryingCharacterId
                        )
                    )
                else:
                    carriedEntity = DofusEntities.getEntity(fighterInfos.contextualId)
                    if carriedEntity:
                        hasCarryingModifier = False
                        if carryingEntity:
                            carryingTs = carryingEntity
                        else:
                            carryingTs = carryingEntity
                        if carryingTs:
                            carryingTs.removeAnimationModifierByClass(
                                CustomBreedAnimationModifier
                            )
                            for modifier in carryingTs.animationModifiers:
                                if isinstance(modifier, CarrierAnimationModifier):
                                    hasCarryingModifier = True
                            if not hasCarryingModifier:
                                carryingTs.addAnimationModifier(
                                    CarrierAnimationModifier()
                                )
                        if not hasCarryingModifier or not (
                            isinstance(carryingEntity, TiphonSprite)
                            and isinstance(carriedEntity, TiphonSprite)
                            and TiphonSprite(carriedEntity).parentSprite
                            == carryingEntity
                        ):
                            self.startCarryStep(
                                fedi.carryingCharacterId, fighterInfos.contextualId
                            )

    def startCarryStep(self, fighterId: float, carriedId: float) -> None:
        step: FightCarryCharacterStep = FightCarryCharacterStep(
            fighterId, carriedId, -1, True
        )
        step.start()
        fightEventsHelper.FightEventsHelper.sendAllFightEvent()

    def updateRemovedEntity(self, idEntity: float) -> None:
        self._entitiesNumber[idEntity] = None
        if Dofus().options.getOption("orderFighters"):
            num = 1
            fightBFrame = (
                krnl.Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
            )
            for entId in fightBFrame.fightersList:
                if entId != idEntity and self.getEntityInfos(entId):
                    self.updateEntityfloat(entId, num)
                    num += 1

    def onPropertyChanged(self, e: PropertyChangeEvent) -> None:
        if not self._worldPoint:
            self._worldPoint = pcm.PlayedCharacterManager().currentMap
        if not self._currentSubAreaId:
            self._currentSubAreaId = pcm.PlayedCharacterManager().currentSubArea.id
        super().onPropertyChanged(e)
        if e.propertyName == "cellSelectionOnly":
            untargetableEntities = (
                e.propertyValue
                or krnl.Kernel().getWorker().getFrame(fightPreparationFrame.FightPreparationFrame)
            )
        elif e.propertyName == "orderFighters":
            if not e.propertyValue:
                for id in self._entitiesNumber:
                    if self._entitiesNumber.get(float(id)):
                        self._entitiesNumber[float(id)] = None
            else:
                num = 1
                fightBFrame = (
                    krnl.Kernel()
                    .getWorker()
                    .getFrame(fightBattleFrame.FightBattleFrame)
                )
                if fightBFrame:
                    for entId in fightBFrame.fightersList:
                        if self.getEntityInfos(entId):
                            num += 1

    @property
    def dematerialization(self) -> bool:
        return self._creaturesFightMode

    @property
    def lastKnownPlayerStatus(self) -> dict:
        return self._lastKnownPlayerStatus

    def getRealFighterLook(self, pFighterId: float) -> EntityLook:
        return self._realFightersLooks[pFighterId]

    def setRealFighterLook(self, pFighterId: float, pEntityLook: EntityLook) -> None:
        self._realFightersLooks[pFighterId] = pEntityLook

    @property
    def charactersMountsVisible(self) -> bool:
        return self._mountsVisible

    def getEntityTeamId(self, entityId: float) -> float:
        if not (entityId in self._entities) or not isinstance(
            self._entities[entityId], GameFightFighterInformations
        ):
            return -1
        entitiesInfo: GameContextActorPositionInformations = self._entities[entityId]
        if not isinstance(entitiesInfo, GameFightFighterInformations):
            return -1
        return entitiesInfo.spawnInfo.teamId

    def getEntityIdsWithTeamId(self, teamId: float) -> list[float]:
        entityInfo: GameFightFighterInformations = None
        entityIds: list[float] = list[float](0)
        if teamId < 0:
            return entityIds
        for entityInfo in self._entities:
            if entityInfo is not None and entityInfo.spawnInfo.teamId == teamId:
                entityIds.append(entityInfo.contextualId)
        return entityIds

    def updateActorDisposition(
        self, actorId: float, newDisposition: EntityDispositionInformations
    ) -> None:
        actor: IEntity = None
        super().updateActorDisposition(actorId, newDisposition)
        if newDisposition.cellId == -1:
            actor = DofusEntities.getEntity(actorId)
            if actor:
                FightEntitiesHolder().holdEntity(actor)
        else:
            FightEntitiesHolder().unholdEntity(actorId)

    def getTmpFighterInfoIndex(self, pId: float) -> float:
        infos: TmpFighterInfos = None
        for infos in self._tempFighterList:
            if infos.contextualId == pId:
                return self._tempFighterList.find(infos)
        return -1


class TmpFighterInfos:

    contextualId: float

    carryingCharacterId: float

    def __init__(self, pId: float, pCarryindId: float):
        super().__init__()
        self.contextualId = pId
        self.carryingCharacterId = pCarryindId

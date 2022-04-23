from com.ankamagames.dofus.datacenter.monsters.Monster import Monster
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
from com.ankamagames.dofus.internalDatacenter.stats.Stat import Stat
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
from com.ankamagames.dofus.logic.game.fight.frames import FightEntitiesFrame
from com.ankamagames.dofus.logic.game.fight.managers.FightersStateManager import (
    FightersStateManager,
)
from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import (
    EntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.FightEntityDispositionInformations import (
    FightEntityDispositionInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.dofus import Constants
from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import (
    GameFightMonsterInformations,
)
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from damageCalculation.tools.StatIds import StatIds
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MouvementPath import MovementPath
from mapTools import MapTools


def getTackle(
    entitiesFrame: FightEntitiesFrame,
    playerInfos: GameFightFighterInformations,
    position: MapPoint,
) -> float:
    stats: EntityStats = StatsManager.getStats(playerInfos.contextualId)
    if Constants.DETERMINIST_TACKLE:
        if not canBeTackled(playerInfos, position):
            return 1
        x = position.x
        y = position.y
        tackleEvadeStat = stats.getStat(StatIds.TACKLE_EVADE)
        evade = int(tackleEvadeStat.totalValue) if tackleEvadeStat is not None else 0
        if evade < 0:
            evade = 0
        entities = list[IEntity]()

        if MapPoint.isInMap(x - 1, y):
            entities.append(getTacklerOnCell(MapTools.getCellIdByCoord(x - 1, y)))

        if MapPoint.isInMap(x + 1, y):
            entities.append(getTacklerOnCell(MapTools.getCellIdByCoord(x + 1, y)))

        if MapPoint.isInMap(x, y - 1):
            entities.append(getTacklerOnCell(MapTools.getCellIdByCoord(x, y - 1)))

        if MapPoint.isInMap(x, y + 1):
            entities.append(getTacklerOnCell(MapTools.getCellIdByCoord(x, y + 1)))

        evadePercent = 1
        for entity in entities:
            if entity:
                infos = entitiesFrame.getEntityInfos(entity.id)
                if canBeTackler(infos, playerInfos):
                    tacklerStats = StatsManager().getStats(entity.id)
                    tackle = (
                        float(tacklerStats.getStatTotalValue(StatIds.TACKLE_BLOCK))
                        if tacklerStats is not None
                        else float(0)
                    )
                    if tackle < 0:
                        tackle = 0
                    mod = (evade + 2) / (tackle + 2) / 2
                    if mod < 1:
                        evadePercent *= mod
        return evadePercent

    return 1


def getTackleForFighter(
    tackler: GameFightFighterInformations, tackled: GameFightFighterInformations
) -> float:
    if not Constants.DETERMINIST_TACKLE:
        return 1
    if not canBeTackled(tackled):
        return 1
    if not canBeTackler(tackler, tackled):
        return 1
    tackledStats: EntityStats = StatsManager.getStats(tackled.contextualId)
    evade: int = (
        int(tackledStats.getStatTotalValue(StatIds.TACKLE_EVADE))
        if tackledStats is not None
        else 0
    )
    if evade < 0:
        evade = 0
    tacklerStats: EntityStats = StatsManager.getStats(tackler.contextualId)
    tackle: int = (
        int(tacklerStats.getStatTotalValue(StatIds.TACKLE_BLOCK))
        if tacklerStats is not None
        else 0
    )
    if tackle < 0:
        tackle = 0
    return (evade + 2) / (tackle + 2) / 2


def getTacklerOnCell(entitiesFrame: FightEntitiesFrame, cellId: int) -> IEntity:
    infos: GameFightFighterInformations = None
    entities: list[IEntity] = EntitiesManager().getEntitiesOnCell(cellId, IEntity)
    for entity in entities:
        infos = entitiesFrame.getEntityInfos(entity.id)
        if infos and isinstance(infos.disposition, EntityDispositionInformations):
            if not FightersStateManager().hasState(
                entity.id, DataEnum.SPELL_STATE_CARRIED
            ):
                return entity
    return None


def canBeTackled(
    fighter: GameFightFighterInformations, position: MapPoint = None
) -> bool:
    fedi: EntityDispositionInformations = None
    if (
        FightersStateManager().hasState(
            fighter.contextualId, DataEnum.SPELL_STATE_CANT_BE_LOCKED
        )
        or FightersStateManager().hasState(
            fighter.contextualId, DataEnum.SPELL_STATE_ROOTED
        )
        or fighter.stats.invisibilityState
        == GameActionFightInvisibilityStateEnum.INVISIBLE
        or fighter.stats.invisibilityState
        == GameActionFightInvisibilityStateEnum.DETECTED
        or FightersStateManager().getStatus(fighter.contextualId).cantBeTackled
    ):
        return False
    if isinstance(fighter.disposition, FightEntityDispositionInformations):
        fedi = fighter.disposition
        if fedi.carryingCharacterId and (
            not position or fighter.disposition.cellId == position.cellId
        ):
            return False

    return True


def canBeTackler(
    entitiesFrame: FightEntitiesFrame,
    fighter: GameFightFighterInformations,
    target: GameFightFighterInformations,
) -> bool:
    monster: Monster = None
    if (
        FightersStateManager().hasState(
            fighter.contextualId, DataEnum.SPELL_STATE_CARRIED
        )
        or FightersStateManager().hasState(
            fighter.contextualId, DataEnum.SPELL_STATE_ROOTED
        )
        or FightersStateManager().hasState(
            fighter.contextualId, DataEnum.SPELL_STATE_CANT_LOCK
        )
        or fighter.stats.invisibilityState
        == GameActionFightInvisibilityStateEnum.INVISIBLE
        or fighter.stats.invisibilityState
        == GameActionFightInvisibilityStateEnum.DETECTED
        or FightersStateManager().getStatus(fighter.contextualId).cantTackle
    ):
        return False
    infos: GameFightFighterInformations = entitiesFrame.getEntityInfos(
        fighter.contextualId
    )
    if infos and infos.spawnInfo.teamId == target.spawnInfo.teamId:
        return False
    if isinstance(fighter, GameFightMonsterInformations):
        monster = monster.getMonsterById(fighter.creatureGenericId)
        if not monster.canTackle:
            return False
    return fighter.spawnInfo.alive


def isTackling(
    pPlayer: GameFightFighterInformations,
    pTackler: GameFightFighterInformations,
    pPlayerPath: MovementPath,
) -> bool:
    stats: EntityStats = StatsManager.getStats(pPlayer.contextualId)
    tackleEvadeStat: Stat = stats.getStat(StatIds.TACKLE_EVADE)
    evade: int = int(tackleEvadeStat.totalValue) if tackleEvadeStat is not None else 0
    tackleBlockStat: Stat = stats.getStat(StatIds.TACKLE_BLOCK)
    block: int = int(tackleBlockStat.totalValue) if tackleBlockStat is not None else 0
    if pPlayerPath and canBeTackler(pTackler, pPlayer):
        for pe in pPlayerPath:
            if canBeTackled(pPlayer, pe.step):
                x = pe.step.x
                y = pe.step.y
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        ac = getTacklerOnCell(MapTools.getCellIdByCoord(i, j))
                        if ac and ac.id == pTackler.contextualId:
                            playerEvasion = 0 if evade < 0 else int(evade)
                            tacklerBlock = 0 if block < 0 else int(block)
                            return (playerEvasion + 2) / (tacklerBlock + 2) / 2 < 1
    return False

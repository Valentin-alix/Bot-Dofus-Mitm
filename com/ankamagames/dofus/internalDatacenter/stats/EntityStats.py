from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.internalDatacenter.stats.DetailedStats import DetailedStat
from com.ankamagames.dofus.internalDatacenter.stats.Stat import Stat
from com.ankamagames.dofus.internalDatacenter.stats.UsableStat import UsableStat
from damageCalculation.tools import StatIds

logger = Logger(__name__)


class EntityStats:
    _entityId: float = None
    _stats: dict

    def __init__(self, entityId: float):
        super().__init__()
        self._entityId = entityId
        self._stats = dict()

    @property
    def entityId(self) -> float:
        return self._entityId

    @property
    def stats(self) -> dict:
        return self._stats

    def getFormattedMessage(self, message: str) -> str:
        return (
            self.__class__.__name__
            + " (Entity ID: "
            + str(self._entityId)
            + "): "
            + message
        )

    def setStat(self, stat: Stat) -> None:
        stat.entityId = self._entityId
        self._stats[stat.id] = stat

    def getStat(self, statId: float) -> Stat:
        if not (statId in self._stats):
            return None
        return str(self._stats[statId])

    def deleteStat(self, statId: float) -> None:
        if not (statId in self._stats):
            return
        statKey: str = str(statId)
        stat: Stat = self._stats[statKey]
        stat.reset()
        del self._stats[statKey]

    def resetStats(self) -> None:
        for stat in self._stats:
            stat.reset()
        self._stats = dict()

    def getStatsfloat(self) -> float:
        counter: float = 0
        for _ in self._stats:
            counter += 1
        return counter

    def hasStat(self, statId: float) -> bool:
        return str(statId) in self._stats

    def getStatTotalValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        return stat is not float(stat.totalValue) if None else float(0)

    def getStatBaseValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, DetailedStat):
            return stat
        return 0

    def getStatAdditionalValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, DetailedStat):
            return stat
        return 0

    def getStatObjectsAndMountBonusValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, DetailedStat):
            return stat
        return 0

    def getStatAlignGiftBonusValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, DetailedStat):
            return stat
        return 0

    def getStatContextModifValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, DetailedStat):
            return stat
        return 0

    def getStatUsedValue(self, statId: float) -> float:
        key: str = str(statId)
        if not (statId in self._stats):
            return 0
        stat: Stat = self._stats[key]
        if isinstance(stat, UsableStat):
            return stat
        return 0

    def __str__(self) -> str:
        statId: float = None
        statsDump: str = ""
        statIds = list[float]()
        stat: Stat = None
        for stat in self._stats:
            statIds.append(stat.id)
        statIds.sort()
        for statId in statIds:
            stat = str(self._stats[statId])
            statsDump += "\n\t" + str(stat)
        if not statsDump:
            statsDump = "\n\tNo stats to display."
        return self.getFormattedMessage(statsDump)

    def getHealthPoints(self) -> float:
        return (
            self.getMaxHealthPoints()
            + self.getStatTotalValue(StatIds.CUR_LIFE)
            + self.getStatTotalValue(StatIds.CUR_PERMANENT_DAMAGE)
        )

    def getMaxHealthPoints(self) -> float:
        detailedVitalityStat: DetailedStat = None
        vitalityStat: Stat = self.getStat(StatIds.VITALITY)
        effectiveVitality: float = 0
        if isinstance(vitalityStat, DetailedStat):
            detailedVitalityStat = vitalityStat
            effectiveVitality = (
                max(
                    0,
                    detailedVitalityStat.baseValue
                    + detailedVitalityStat.objectsAndMountBonusValue
                    + detailedVitalityStat.additionalValue
                    + detailedVitalityStat.alignGiftBonusValue,
                )
                + detailedVitalityStat.contextModifValue
            )
        elif isinstance(vitalityStat, Stat):
            effectiveVitality = vitalityStat.totalValue
        return (
            self.getStatTotalValue(StatIds.LIFE_POINTS)
            + effectiveVitality
            - self.getStatTotalValue(StatIds.CUR_PERMANENT_DAMAGE)
        )

from typing import TYPE_CHECKING
from com.ankamagames.dofus.datacenter.monsters.AnimFunMonsterData import (
    AnimFunMonsterData,
)

if TYPE_CHECKING:
    from com.ankamagames.dofus.datacenter.monsters.MonsterDrop import MonsterDrop
    from com.ankamagames.dofus.datacenter.monsters.MonsterGrade import MonsterGrade
    from com.ankamagames.dofus.datacenter.monsters.MonsterRace import MonsterRace
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class Monster:

    MODULE: str = "Monsters"

    @classmethod
    def getMonsterById(cls, id: int) -> "Monster":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getMonsters(cls) -> list:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getMonsterById, getMonsters)

    id: int

    nameId: int

    gfxId: int

    race: int

    grades: list["MonsterGrade"]

    look: str

    useSummonSlot: bool

    useBombSlot: bool

    canPlay: bool

    canTackle: bool

    animFunList: list[AnimFunMonsterData]

    isBoss: bool

    drops: list["MonsterDrop"]

    temporisDrops: list["MonsterDrop"]

    subareas: list[int]

    spells: list[int]

    favoriteSubareaId: int

    isMiniBoss: bool

    isQuestMonster: bool

    correspondingMiniBossId: int

    speedAdjust: float = 0.0

    creatureBoneId: int

    canBePushed: bool

    canBeCarried: bool

    canUsePortal: bool

    canSwitchPos: bool

    canSwitchPosOnTarget: bool

    fastAnimsFun: bool

    incompatibleIdols: list[int]

    allIdolsDisabled: bool

    incompatibleChallenges: list[int]

    useRaceValues: bool

    aggressiveZoneSize: int

    aggressiveLevelDiff: int

    aggressiveImmunityCriterion: str

    aggressiveAttackDelay: int

    scaleGradeRef: int

    characRatios: list[list[float]]

    _name: str

    _undiatricalName: str

    @property
    def type(self) -> "MonsterRace":
        from com.ankamagames.dofus.datacenter.monsters.MonsterRace import MonsterRace

        return MonsterRace.getMonsterRaceById(self.race)

    @property
    def isAggressive(self) -> bool:
        return self.aggressiveZoneSize > 0

    @property
    def canAttack(self) -> bool:
        if self.aggressiveImmunityCriterion:
            from com.ankamagames.dofus.datacenter.items.criterion import (
                GroupItemCriterion,
            )

            criterions = GroupItemCriterion(self.aggressiveImmunityCriterion)
            if criterions.isRespected:
                return False
        return True

    def getMonsterGrade(self, grade: int) -> "MonsterGrade":
        if grade < 1 or grade > len(self.grades):
            grade = len(self.grades)
        return self.grades[grade - 1]

    def getAggressionLevel(self, grade: int) -> int:
        return self.grades[grade - 1].level - self.aggressiveLevelDiff

    def getCharacRatio(self, characId: int) -> float:
        charac: list[float] = None
        for charac in self.characRatios:
            if characId == int(charac[0]):
                return charac[1]
        return 1

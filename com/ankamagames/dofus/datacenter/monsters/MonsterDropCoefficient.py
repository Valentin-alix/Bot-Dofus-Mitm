from com.ankamagames.dofus.datacenter.items.criterion import GroupItemCriterion
from com.ankamagames.dofus.datacenter.monsters.Monster import Monster


class MonsterDropCoefficient:

    monsterId: int

    monsterGrade: int

    dropCoefficient: float

    criteria: str

    _monster: Monster

    _conditions: GroupItemCriterion

    @property
    def monster(self) -> Monster:
        if not self._monster:
            self._monster = Monster.getMonsterById(self.monsterId)
        return self._monster

    @property
    def conditions(self) -> GroupItemCriterion:
        if not self.criteria:
            return None
        if not self._conditions:
            self._conditions = GroupItemCriterion(self.criteria)
        return self._conditions

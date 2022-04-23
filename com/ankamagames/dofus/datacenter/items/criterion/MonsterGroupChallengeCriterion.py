from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class MonsterGroupChallengeCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(self._criterionValue + 1)
        return I18n.getUiText(
            "ui.breachReward.groupChallengCriterion", [readableCriterionValue]
        )

    def clone(self) -> IItemCriterion:
        return MonsterGroupChallengeCriterion(self.basicText)

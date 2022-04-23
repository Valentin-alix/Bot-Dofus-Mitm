from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class SubscribeItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        if (
            self._criterionValue == 1
            and self._operator.text == ItemCriterionOperator.EQUAL
            or self._criterionValue == 0
            and self._operator.text == ItemCriterionOperator.DIFFERENT
        ):
            return I18n.getUiText("ui.tooltip.beSubscirber")
        return I18n.getUiText("ui.tooltip.dontBeSubscriber")

    def clone(self) -> IItemCriterion:
        return SubscribeItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        timeRemaining: float = PlayerManager().subscriptionEndDate
        if timeRemaining > 0 or PlayerManager().hasRights:
            return 1
        return 0

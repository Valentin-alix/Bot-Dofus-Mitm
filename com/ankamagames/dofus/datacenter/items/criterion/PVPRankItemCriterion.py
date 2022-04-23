from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class PVPRankItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        return (
            I18n.getUiText("ui.pvp.rank")
            + " "
            + self._operator.text
            + " "
            + self._criterionValue
        )

    def clone(self) -> IItemCriterion:
        return PVPRankItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

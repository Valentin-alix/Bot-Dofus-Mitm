from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.data import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class UnusableItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        return I18n.getUiText("ui.criterion.unusableItem")

    @property
    def isRespected(self) -> bool:
        return True

    def clone(self) -> IItemCriterion:
        return UnusableItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

from pyd2bot.dofus.datacenter.items.IItemCriterion import IItemCriterion
from pyd2bot.dofus.datacenter.items.ItemCriterion import ItemCriterion


class StaticCriterionItemCriterion(ItemCriterion):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        return ""

    @property
    def isRespected(self) -> bool:
        return True

    def clone(self) -> IItemCriterion:
        return StaticCriterionItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

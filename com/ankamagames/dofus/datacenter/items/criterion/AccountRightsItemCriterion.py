from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion


class AccountRightsItemCriterion(ItemCriterion):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    def clone(self) -> "AccountRightsItemCriterion":
        return AccountRightsItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

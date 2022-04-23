class BonusSetItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = I18n.getUiText("ui.criterion.setBonus")
        return readableCriterionRef + " " + _operator.text + " " + _criterionValue

    @property
    def isRespected(self) -> bool:
        return _operator.compare(int(self.getCriterion()), _criterionValue)

    def clone(self) -> IItemCriterion:
        return BonusSetItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        iw: ItemWrapper = None
        bonusPerSet: int = 0
        nbBonus: int = 0
        sets: dict = dict()
        for iw in InventoryManager().inventory.getView("equipment").content:
            if iw:
                if iw.itemSetId > 0:
                    if sets[iw.itemSetId] > 0:
                        sets[iw.itemSetId] += 1
                    if sets[iw.itemSetId] == -1:
                        sets[iw.itemSetId] = 1
                    if not sets[iw.itemSetId]:
                        sets[iw.itemSetId] = -1
        for bonusPerSet in sets:
            if bonusPerSet > 0:
                nbBonus += bonusPerSet
        return nbBonus

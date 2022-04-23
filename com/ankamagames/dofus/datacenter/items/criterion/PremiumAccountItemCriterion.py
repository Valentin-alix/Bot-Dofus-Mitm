class PremiumAccountItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterion: str = I18n.getUiText("ui.tooltip.possessPremiumAccount")
        if _criterionValue == 0:
            readableCriterion = I18n.getUiText("ui.tooltip.dontPossessPremiumAccount")
        return readableCriterion

    def clone(self) -> IItemCriterion:
        return PremiumAccountItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

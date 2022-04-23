class NewHavenbagItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = None
        havenbagTheme: str = HavenbagTheme.getTheme(_criterionValue).name
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterionRef = I18n.getUiText(
                "ui.criterion.notHavenbagTheme", [havenbagTheme]
            )
        else:
            readableCriterionRef = I18n.getUiText(
                "ui.criterion.hasHavenbagTheme", [havenbagTheme]
            )
        return readableCriterionRef

    def clone(self) -> IItemCriterion:
        return NewHavenbagItemCriterion(self.basicText)

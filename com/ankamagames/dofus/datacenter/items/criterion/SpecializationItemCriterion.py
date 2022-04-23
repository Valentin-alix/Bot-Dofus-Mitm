class SpecializationItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = AlignmentRank.getAlignmentRankById(
            int(_criterionValue)
        ).name
        readableCriterionRef: str = I18n.getUiText("ui.alignment.sp�cialization")
        readableOperator: str = I18n.getUiText("ui.common.colon")
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = (
                " "
                + I18n.getUiText("ui.common.differentFrom")
                + I18n.getUiText("ui.common.colon")
            )
        return readableCriterionRef + readableOperator + readableCriterionValue

    def clone(self) -> IItemCriterion:
        return SpecializationItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return AlignmentFrame().playerRank

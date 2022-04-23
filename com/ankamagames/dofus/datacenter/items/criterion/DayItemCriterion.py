class DayItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(_criterionValue)
        readableCriterionRef: str = PatternDecoder.combine(
            I18n.getUiText("ui.time.days"), "n", True
        )
        return (
            readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return DayItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        date: Date = Date()
        return TimeManager().getDateFromTime(date.getTime())[2]

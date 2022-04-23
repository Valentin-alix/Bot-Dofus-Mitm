class MonthItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = Month.getMonthById(_criterionValue).name
        readableCriterionRef: str = I18n.getUiText("ui.time.months")
        return (
            readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return MonthItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        date: Date = Date()
        monthInt: int = TimeManager().getDateFromTime(date.getTime())[3]
        return monthInt - 1

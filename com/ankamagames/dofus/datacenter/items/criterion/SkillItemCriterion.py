class SkillItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        return _criterionRef + " " + _operator.text + " " + _criterionValue

    def clone(self) -> IItemCriterion:
        return SkillItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return 0

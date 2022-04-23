class SexItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        if _criterionValue == 1:
            return I18n.getUiText("ui.tooltip.beFemale")
        return I18n.getUiText("ui.tooltip.beMale")

    def clone(self) -> IItemCriterion:
        return SexItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return int(PlayedCharacterManager().infos.sex)

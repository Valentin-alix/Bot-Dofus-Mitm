class BreedItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = Breed.getBreedById(float(_criterionValue)).shortName
        if _operator.text == ItemCriterionOperator.EQUAL:
            return I18n.getUiText("ui.tooltip.beABreed", [readableCriterionRef])
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            return I18n.getUiText("ui.tooltip.dontBeABreed", [readableCriterionRef])
        return ""

    def clone(self) -> IItemCriterion:
        return BreedItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return int(PlayedCharacterManager().infos.breed)

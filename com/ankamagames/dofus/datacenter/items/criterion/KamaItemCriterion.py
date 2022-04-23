class KamaItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = I18n.getUiText("ui.common.kamas")
        return readableCriterionRef + " " + _operator.text + " " + _criterionValue

    @property
    def isRespected(self) -> bool:
        return _operator.compare(
            PlayedCharacterManager().characteristics.kamas, _criterionValue
        )

    def clone(self) -> IItemCriterion:
        return KamaItemCriterion(self.basicText)

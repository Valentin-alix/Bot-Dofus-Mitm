class PrestigeLevelItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(_criterionValue)
        readableCriterionRef: str = I18n.getUiText("ui.common.prestige")
        return (
            readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return PrestigeLevelItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        prestige: int = 0
        if PlayedCharacterManager().infos.level > ProtocolConstantsEnum.MAX_LEVEL:
            prestige = (
                PlayedCharacterManager().infos.level - ProtocolConstantsEnum.MAX_LEVEL
            )
        return prestige

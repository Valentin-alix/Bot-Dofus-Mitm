class BonesItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        if _criterionValue == 0 and _criterionValueText == "B":
            return I18n.getUiText("ui.criterion.initialBones")
        return (
            I18n.getUiText("ui.criterion.bones")
            + " "
            + _operator.text
            + " "
            + str(_criterionValue)
        )

    @property
    def isRespected(self) -> bool:
        if _criterionValue == 0 and _criterionValueText == "B":
            return PlayedCharacterManager().infos.entityLook.bonesId == 1
        return PlayedCharacterManager().infos.entityLook.bonesId == _criterionValue

    def clone(self) -> IItemCriterion:
        return BonesItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return PlayedCharacterManager().infos.entityLook.bonesId

class RideItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterion: str = None
        mountModel: Mount = Mount.getMountById(_criterionValue)
        if _criterionValue == 0 or not mountModel:
            return ""
        if _operator.text == ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText(
                "ui.tooltip.mountEquiped", [mountModel.name]
            )
        elif _operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText(
                "ui.tooltip.mountNonEquiped", [mountModel.name]
            )
        return readableCriterion

    def clone(self) -> IItemCriterion:
        return RideItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        mountId: int = 0
        mount: MountData = PlayedCharacterManager().mount
        if mount and PlayedCharacterManager().isRidding:
            mountId = mount.modelId
        return mountId

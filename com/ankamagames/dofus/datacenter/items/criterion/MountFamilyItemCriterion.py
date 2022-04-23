class MountFamilyItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = None
        mountFamily: MountFamily = MountFamily.getMountFamilyById(
            float(_criterionValue)
        )
        if not mountFamily:
            readableCriterionRef = "???"
        else:
            readableCriterionRef = mountFamily.name
        if _operator.text == ItemCriterionOperator.EQUAL:
            return I18n.getUiText(
                "ui.tooltip.mountEquipedFamily", [readableCriterionRef]
            )
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            return I18n.getUiText(
                "ui.tooltip.mountNonEquipedFamily", [readableCriterionRef]
            )
        return ""

    def clone(self) -> IItemCriterion:
        return MountFamilyItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        mount: MountData = PlayedCharacterManager().mount
        if not mount or not PlayedCharacterManager().isRidding:
            return -1
        return mount.model.familyId

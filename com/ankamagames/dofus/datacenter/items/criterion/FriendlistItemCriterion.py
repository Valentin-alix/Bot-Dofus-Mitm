class FriendlistItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionRef: str = I18n.getUiText("ui.tooltip.playerInFriendlist")
        readableOperator: str = _operator.text
        if readableOperator == ItemCriterionOperator.EQUAL:
            readableOperator = ":"
        return readableCriterionRef + " " + readableOperator + " " + _criterionValue

    def clone(self) -> IItemCriterion:
        return FriendlistItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        returnKernel().getWorker().getFrame(SocialFrame)

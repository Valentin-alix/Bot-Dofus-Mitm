class SmileyPackItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def isRespected(self) -> bool:
        pack: SmileyPack = None
        packList: list = Kernel().getWorker().getFrame(ChatFrame)
        for pack in packList:
            if pack.id == _criterionValue:
                return False
        return True

    @property
    def text(self) -> str:
        readableCriterion: str = None
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.tooltip.dontPossessSmileyPack")
        else:
            readableCriterion = I18n.getUiText("ui.tooltip.possessSmileyPack")
        return (
            readableCriterion
            + " '"
            + SmileyPack.getSmileyPackById(_criterionValue).name
            + "'"
        )

    def clone(self) -> IItemCriterion:
        return SmileyPackItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        pack: SmileyPack = None
        packList: list = Kernel().getWorker().getFrame(ChatFrame)
        for pack in packList:
            if pack.id == _criterionValue:
                return 1
        return 0

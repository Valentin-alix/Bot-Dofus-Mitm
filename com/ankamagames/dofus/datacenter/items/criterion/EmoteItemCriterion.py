class EmoteItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    def getEmotesList(self) -> list:
        emoticonFrame: EmoticonFrame = Kernel().getWorker().getFrame(EmoticonFrame)
        if emoticonFrame:
            return emoticonFrame.emotesList
        return None

    @property
    def isRespected(self) -> bool:
        emoteWrapper: EmoteWrapper = None
        for emoteWrapper in self.getEmotesList():
            if emoteWrapper.emote.id == _criterionValue:
                return False
        return True

    @property
    def text(self) -> str:
        readableCriterion: str = I18n.getUiText("ui.tooltip.possessEmote")
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.tooltip.dontPossessEmote")
        return (
            readableCriterion
            + " '"
            + Emoticon.getEmoticonById(_criterionValue).name
            + "'"
        )

    def clone(self) -> IItemCriterion:
        return EmoteItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        id: int = 0
        for id in self.getEmotesList():
            if id == _criterionValue:
                return 1
        return 0

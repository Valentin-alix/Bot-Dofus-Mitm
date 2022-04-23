class GuildItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        if _criterionValue == 0:
            return I18n.getUiText("ui.criterion.noguild")
        return I18n.getUiText("ui.criterion.hasGuild")

    def clone(self) -> IItemCriterion:
        return GuildItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        guild: GuildWrapper = Kernel().getWorker().getFrame(SocialFrame)
        if guild:
            return 1
        return 0

class GuildLevelItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(_criterionValue)
        readableCriterionRef: str = I18n.getUiText("ui.guild.guildLevel")
        return (
            readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return GuildLevelItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        guild: GuildWrapper = Kernel().getWorker().getFrame(SocialFrame)
        if guild:
            return guild.level
        return 0

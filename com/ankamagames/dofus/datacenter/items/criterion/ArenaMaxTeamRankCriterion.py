class ArenaMaxTeamRankCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(_criterionValue)
        readableCriterionRef: str = I18n.getUiText("ui.common.pvpMaxTeamRank")
        readableOperator = ">"
        if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
        return (
            readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return ArenaMaxTeamRankCriterion(self.basicText)

    def getCriterion(self) -> int:
        frame: PartyManagementFrame = (
            Kernel().getWorker().getFrame(PartyManagementFrame)
        )
        maxRank: int = 0
        if frame.arenaRankGroupInfos and frame.arenaRankGroupInfos.maxRank > maxRank:
            maxRank = frame.arenaRankGroupInfos.maxRank
        return maxRank

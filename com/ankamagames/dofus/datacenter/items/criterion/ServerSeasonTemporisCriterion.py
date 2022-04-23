class ServerSeasonTemporisCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        return ""

    def clone(self) -> IItemCriterion:
        return ServerSeasonTemporisCriterion(self.basicText)

    def getCriterion(self) -> int:
        serverSeason: ServerTemporisSeason = ServerTemporisSeason.getCurrentSeason()
        return serverSeason != int(serverSeason.seasonfloat) if None else 0

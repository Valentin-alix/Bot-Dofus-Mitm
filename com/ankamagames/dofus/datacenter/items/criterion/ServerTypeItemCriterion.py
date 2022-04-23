class ServerTypeItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def isRespected(self) -> bool:
        if _operator.compare(PlayerManager().serverGameType, _criterionValue):
            return True
        return False

    @property
    def text(self) -> str:
        return ""

    def clone(self) -> IItemCriterion:
        return ServerTypeItemCriterion(self.basicText)

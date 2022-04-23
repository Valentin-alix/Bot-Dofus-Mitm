class ServerItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = Server.getServerById(_criterionValue).name
        readableCriterionRef: str = I18n.getUiText("ui.header.server")
        return (
            readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return ServerItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return PlayerManager().server.id

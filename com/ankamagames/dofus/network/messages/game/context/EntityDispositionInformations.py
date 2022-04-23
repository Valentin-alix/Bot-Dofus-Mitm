class EntityDispositionInformations:
    cellId: int = 0
    direction: int = 1

    def __init__(self):
        super().__init__()

    def initEntityDispositionInformations(
        self, cellId: int = 0, direction: int = 1
    ) -> "EntityDispositionInformations":
        self.cellId = cellId
        self.direction = direction
        return self

    def reset(self) -> None:
        self.cellId = 0
        self.direction = 1

from com.ankamagames.atouin.messages.CellInteractionMessage import (
    CellInteractionMessage,
)


class CellClickMessage(CellInteractionMessage):

    fromStack: bool

    fromAutotrip: bool

    def __init__(self, cellId: int = 0, mapId: float = 0):
        super().__init__()
        self.cellId = cellId
        self.id = mapId

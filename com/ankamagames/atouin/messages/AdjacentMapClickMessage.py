from com.ankamagames.jerakine.messages.Message import Message


class AdjacentMapClickMessage(Message):

    adjacentMapId: float

    cellId: int

    fromStack: bool

    fromAutotrip: bool

    def __init__(self):
        super().__init__()

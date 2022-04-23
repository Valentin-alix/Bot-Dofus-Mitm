from com.ankamagames.jerakine.messages.Message import Message


class DelayedActionMessage(Message):

    _playerId: float

    _itemId: int

    _endTime: float

    def __init__(self, playerId: float, itemId: int, endTime: float):
        super().__init__()
        self._playerId = playerId
        self._itemId = itemId
        self._endTime = endTime

    @property
    def playerId(self) -> float:
        return self._playerId

    @property
    def itemId(self) -> int:
        return self._itemId

    @property
    def endTime(self) -> float:
        return self._endTime

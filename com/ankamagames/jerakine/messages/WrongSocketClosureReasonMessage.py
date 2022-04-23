from com.ankamagames.jerakine.messages.Message import Message


class WrongSocketClosureReasonMessage(Message):

    _expectedReason: int

    _gotReason: int

    def __init__(self, expectedReason: int, gotReason: int):
        super().__init__()
        self._expectedReason = expectedReason
        self._gotReason = gotReason

    @property
    def expectedReason(self) -> int:
        return self._expectedReason

    @property
    def gotReason(self) -> int:
        return self._gotReason

from com.ankamagames.jerakine.messages.Message import Message


class MapMessage(Message):

    _id: float

    _transitionType: str

    renderRequestId: int

    def __init__(self):
        super().__init__()

    @property
    def id(self) -> float:
        return self._id

    @id.setter
    def id(self, nValue: float) -> None:
        self._id = nValue

    @property
    def transitionType(self) -> str:
        return self._transitionType

    @transitionType.setter
    def transitionType(self, sValue: str) -> None:
        self._transitionType = sValue

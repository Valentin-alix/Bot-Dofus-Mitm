from com.ankamagames.jerakine.messages.Message import Message


class ExpectedSocketClosureMessage(Message):

    reason: int

    def __init__(self, reason: int = 0):
        super().__init__()
        self.reason = reason

from com.ankamagames.dofus.network.messages.queues.LoginQueueStatusMessage import (
    LoginQueueStatusMessage,
)
from com.ankamagames.dofus.network.messages.queues.QueueStatusMessage import (
    QueueStatusMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority


class QueueFrame(Frame):
    def __init__(self):
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    def pushed(self) -> bool:
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, LoginQueueStatusMessage):
            return True

        elif isinstance(msg, QueueStatusMessage):
            return True

        else:
            return False

    def pulled(self) -> bool:
        return True

from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.network.messages.game.basic.SequenceNumberMessage import (
    SequenceNumberMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from com.ankamagames.dofus.network.messages.game.basic.SequenceNumberRequestMessage import (
    SequenceNumberRequestMessage,
)

logger = Logger(__name__)


class SynchronisationFrame(Frame):

    STEP_TIME: int = 2

    def __init__(self):
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.HIGHEST

    def pushed(self) -> bool:
        self._synchroStepByServer = dict()
        return True

    def resetSynchroStepByServer(self, connexionId: str) -> None:
        self._synchroStepByServer[connexionId] = 0

    def process(self, msg: Message) -> bool:
        snrMsg: SequenceNumberRequestMessage = None
        snMsg: SequenceNumberMessage = None

        if isinstance(msg, SequenceNumberRequestMessage):
            snrMsg = msg
            if not self._synchroStepByServer.get(snrMsg.sourceConnection):
                self._synchroStepByServer[snrMsg.sourceConnection] = 0
            self._synchroStepByServer[snrMsg.sourceConnection] += 1
            snMsg = SequenceNumberMessage()
            snMsg.init(number_=self._synchroStepByServer[snrMsg.sourceConnection])
            ConnectionsHandler.getConnection().send(snMsg, snrMsg.sourceConnection)
            return True

        else:
            return False

    def pulled(self) -> bool:
        return True

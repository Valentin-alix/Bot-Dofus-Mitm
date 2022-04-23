from logging import Logger
from time import perf_counter, perf_counter_ns
from com.ankamagames.dofus import Constants
import com.ankamagames.dofus.kernel.Kernel as krnl
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.kernel.net.DisconnectionReasonEnum import (
    DisconnectionReasonEnum,
)
from com.ankamagames.jerakine.benchmark.BenchmarkTimer import BenchmarkTimer
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.messages.WrongSocketClosureReasonMessage import (
    WrongSocketClosureReasonMessage,
)
from com.ankamagames.jerakine.network.ServerConnectionClosedMessage import (
    ServerConnectionClosedMessage,
)
from com.ankamagames.jerakine.network.messages.ExpectedSocketClosureMessage import (
    ExpectedSocketClosureMessage,
)
from com.ankamagames.jerakine.network.messages.UnexpectedSocketClosureMessage import (
    UnexpectedSocketClosureMessage,
)
from com.ankamagames.jerakine.types.enums.Priority import Priority
import com.ankamagames.dofus.logic.game.approach.frames.GameServerApproachFrame as gsaF

logger = Logger(__name__)


class DisconnectionHandlerFrame(Frame):

    CONNECTION_ATTEMPTS_NUMBER: int = 4

    messagesAfterReset: list = list()

    _connectionUnexpectedFailureTimes: list

    _numberOfAttemptsAlreadyDone: int = 0

    _timer: BenchmarkTimer

    _mustShowLoginInterface: bool = False

    def __init__(self):
        self._connectionUnexpectedFailureTimes = list()
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.LOW

    def resetConnectionAttempts(self) -> None:
        self._connectionUnexpectedFailureTimes = list()
        StoreDataManager().setData(
            Constants.DATASTORE_MODULE_DEBUG, "connection_fail_times", None
        )
        self._numberOfAttemptsAlreadyDone = 0

    def pushed(self) -> bool:
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, ServerConnectionClosedMessage):
            sccmsg = msg
            if (
                connh.ConnectionsHandler.getConnection()
                and connh.ConnectionsHandler.getConnection().mainConnection
                and (
                    connh.ConnectionsHandler.getConnection().mainConnection.connected
                    or connh.ConnectionsHandler.getConnection().mainConnection.connecting
                )
            ):
                return False

            if (
                sccmsg.closedConnection
                == connh.ConnectionsHandler.getConnection().getSubConnection(sccmsg)
            ):
                logger.debug("The connection was closed. Checking reasons.")
                gsaF.GameServerApproachFrame.authenticationTicketAccepted = False
                if connh.ConnectionsHandler.hasReceivedMsg:
                    if (
                        not connh.ConnectionsHandler.hasReceivedNetworkMsg
                        and self._numberOfAttemptsAlreadyDone
                        < self.CONNECTION_ATTEMPTS_NUMBER
                    ):
                        self._numberOfAttemptsAlreadyDone += 1
                        logger.warn(
                            f"The connection was closed unexpectedly. Reconnection attempt {self._numberOfAttemptsAlreadyDone}/{self.CONNECTION_ATTEMPTS_NUMBER} will start in 4s."
                        )
                        self._connectionUnexpectedFailureTimes.append(perf_counter())
                        StoreDataManager().setData(
                            Constants.DATASTORE_MODULE_DEBUG,
                            "connection_fail_times",
                            self._connectionUnexpectedFailureTimes,
                        )
                    else:
                        reason = connh.ConnectionsHandler.handleDisconnection()
                        if not reason.expected:
                            logger.warn(
                                "The connection was closed unexpectedly. Reseting."
                            )
                            if (
                                self._numberOfAttemptsAlreadyDone
                                == self.CONNECTION_ATTEMPTS_NUMBER
                            ):
                                self._connectionUnexpectedFailureTimes.append(
                                    perf_counter()
                                )
                                StoreDataManager().setData(
                                    Constants.DATASTORE_MODULE_DEBUG,
                                    "connection_fail_times",
                                    self._connectionUnexpectedFailureTimes,
                                )
                            if len(self.messagesAfterReset) == 0:
                                self.messagesAfterReset = [
                                    UnexpectedSocketClosureMessage()
                                ] + self.messagesAfterReset
                            krnl.Kernel().reset()
                        else:
                            logger.debug(
                                f"The connection closure was expected (reason: {reason.reason}). Dispatching the message."
                            )
                            if (
                                reason.reason
                                == DisconnectionReasonEnum.DISCONNECTED_BY_POPUP
                                or reason.reason
                                == DisconnectionReasonEnum.SWITCHING_TO_HUMAN_VENDOR
                            ):
                                krnl.Kernel().reset()
                            else:
                                krnl.Kernel().getWorker().process(
                                    ExpectedSocketClosureMessage(reason.reason)
                                )
                else:
                    logger.warn("The connection hasn't even start.")
            return True

        elif isinstance(msg, WrongSocketClosureReasonMessage):
            wscrmsg = msg
            gsaF.GameServerApproachFrame.authenticationTicketAccepted = False
            logger.error(
                "Expecting socket closure for reason "
                + wscrmsg.expectedReason
                + ", got reason "
                + wscrmsg.gotReason
                + "! Reseting."
            )
            krnl.Kernel().reset([UnexpectedSocketClosureMessage()])
            return True

        elif isinstance(msg, UnexpectedSocketClosureMessage):
            logger.debug("go hook UnexpectedSocketClosure")
            gsaF.GameServerApproachFrame.authenticationTicketAccepted = False
            return True

    def pulled(self) -> bool:
        return True

from time import perf_counter
from com.ankamagames.dofus import Constants
import com.ankamagames.dofus.kernel.Kernel as krnl
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
import com.ankamagames.dofus.logic.connection.frames.ServerSelectionFrame as ssfrm
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.dofus.logic.common.managers.InterClientManager import (
    InterClientManager,
)
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.connection.frames.DisconnectionHandlerFrame import (
    DisconnectionHandlerFrame,
)
from com.ankamagames.dofus.network.enums.IdentificationFailureReasonsEnum import (
    IdentificationFailureReasonEnum,
)
from com.ankamagames.dofus.network.messages.connection.HelloConnectMessage import (
    HelloConnectMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationAccountForceMessage import (
    IdentificationAccountForceMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import (
    IdentificationFailedMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import (
    IdentificationSuccessMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessWithLoginTokenMessage import (
    IdentificationSuccessWithLoginTokenMessage,
)
from com.ankamagames.dofus.network.messages.security.ClientKeyMessage import (
    ClientKeyMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import (
    ServerConnectionFailedMessage,
)
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.Priority import Priority

logger = Logger(__name__)


class AuthentificationFrame(Frame):

    HIDDEN_PORT: int = 443

    CONNEXION_MODULE_NAME: str = "ComputerModule_Ankama_Connection"

    _lastTicket: str

    _connexionHosts: list = []

    _dispatchModuleHook: bool = False

    _connexionSequence: list

    _lastLoginHash: str

    _currentLogIsForced: bool = False

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    def handleConnectionOpened(self) -> None:
        pass

    def handleConnectionClosed(self) -> None:
        pass

    def process(self, msg: Message) -> bool:

        if isinstance(msg, ServerConnectionFailedMessage):
            scfMsg = msg
            if (
                scfMsg.failedConnection
                == connh.ConnectionsHandler.getConnection().getSubConnection(scfMsg)
            ):
                connh.ConnectionsHandler.getConnection().mainConnection.stopConnectionTimeout()
                if self._connexionSequence:
                    retryConnInfo = self._connexionSequence.pop(0)
                    if retryConnInfo:
                        connh.ConnectionsHandler.connectToLoginServer(
                            retryConnInfo.host, retryConnInfo.port
                        )
                    else:
                        PlayerManager().destroy()
            return True

        elif isinstance(msg, HelloConnectMessage):
            hcmsg = msg
            AuthentificationManager().setPublicKey(hcmsg.key)
            AuthentificationManager().setSalt(hcmsg.salt)
            AuthentificationManager().initAESKey()
            iMsg = AuthentificationManager().getIdentificationMessage()
            self._currentLogIsForced = isinstance(
                iMsg, IdentificationAccountForceMessage
            )
            # Plogger.info(f"Current version : {iMsg.version.major}.{iMsg.version.minor}.{iMsg.version.code}.{iMsg.version.build}")
            dhf = krnl.Kernel().getWorker().getFrame(DisconnectionHandlerFrame)
            time = perf_counter()
            elapsedTimesSinceConnectionFail = list[int]()
            failureTimes = StoreDataManager().getData(
                Constants.DATASTORE_MODULE_DEBUG, "connection_fail_times"
            )
            if failureTimes:
                for i in range(len(failureTimes)):
                    elapsedSeconds = time - failureTimes[i]
                    if elapsedSeconds <= 3600:
                        elapsedTimesSinceConnectionFail[i] = elapsedSeconds
                dhf.resetConnectionAttempts()
            iMsg.failedAttempts = elapsedTimesSinceConnectionFail
            connh.ConnectionsHandler.getConnection().send(iMsg)
            if InterClientManager().flashKey:
                flashKeyMsg = ClientKeyMessage()
                flashKeyMsg.key = InterClientManager().flashKey
                connh.ConnectionsHandler.getConnection().send(flashKeyMsg)
            return True

        elif isinstance(msg, IdentificationSuccessMessage):
            ismsg = msg
            if isinstance(ismsg, IdentificationSuccessWithLoginTokenMessage):
                AuthentificationManager().nextToken = (
                    IdentificationSuccessWithLoginTokenMessage(ismsg).loginToken
                )
            if ismsg.login:
                AuthentificationManager().username = ismsg.login
            PlayerManager().accountId = ismsg.accountId
            PlayerManager().communityId = ismsg.communityId
            PlayerManager().hasRights = ismsg.hasRights
            PlayerManager().hasConsoleRight = ismsg.hasConsoleRight
            PlayerManager().nickname = ismsg.accountTag.nickname
            PlayerManager().tag = ismsg.accountTag.tagNumber
            PlayerManager().subscriptionEndDate = ismsg.subscriptionEndDate
            PlayerManager().subscriptionDurationElapsed = (
                ismsg.subscriptionElapsedDuration
            )
            PlayerManager().secretQuestion = ismsg.secretQuestion
            PlayerManager().accountCreation = ismsg.accountCreation
            PlayerManager().wasAlreadyConnected = ismsg.wasAlreadyConnected
            DataStoreType.ACCOUNT_ID = str(ismsg.accountId)
            StoreDataManager().setData(
                Constants.DATASTORE_COMPUTER_OPTIONS, "lastAccountId", ismsg.accountId
            )
            krnl.Kernel().getWorker().removeFrame(self)
            krnl.Kernel().getWorker().addFrame(ssfrm.ServerSelectionFrame())
            return True

        elif isinstance(msg, IdentificationFailedMessage):
            logger.info(
                "Identification failed for reason "
                + IdentificationFailureReasonEnum(msg.reason).name
            )
            PlayerManager().destroy()
            connh.ConnectionsHandler.closeConnection()
            if not self._dispatchModuleHook:
                self._dispatchModuleHook = True
                self.pushed()
            return True

    def pushed(self) -> bool:
        return True

    def pulled(self) -> bool:
        return True

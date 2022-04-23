from ctypes import ArgumentError
from threading import Timer
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.logic.common.utils.LagometerAck import LagometerAck
from com.ankamagames.dofus.logic.connection.frames.HandshakeFrame import HandshakeFrame
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.ConnectionResumedMessage import (
    ConnectionResumedMessage,
)
from com.ankamagames.jerakine.network.IConnectionProxy import IConnectionProxy
from com.ankamagames.jerakine.network.IServerConnection import IServerConnection
from com.ankamagames.dofus.kernel.net.ConnectionType import ConnectionType
from com.ankamagames.dofus.kernel.net.DisconnectionReason import DisconnectionReason
from com.ankamagames.dofus.kernel.net.DisconnectionReasonEnum import (
    DisconnectionReasonEnum,
)
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.network.messages.common.basic.BasicPingMessage import (
    BasicPingMessage,
)
from com.ankamagames.jerakine.network.MultiConnection import MultiConnection
from com.ankamagames.jerakine.network.ServerConnection import ServerConnection
from com.ankamagames.dofus.network.MessageReceiver import MessageReceiver

logger = Logger(__name__)


class ConnectionsHandler:

    GAME_SERVER: str = "game_server"

    KOLI_SERVER: str = "koli_server"

    _useSniffer: bool = False

    _currentConnection: MultiConnection = None

    _currentConnectionType: str = None

    _wantedSocketLost: bool = False

    _wantedSocketLostReason: int = 0

    _hasReceivedMsg: bool = False

    _hasReceivedNetworkMsg: bool = False

    _connectionTimeout = None

    @property
    @classmethod
    def useSniffer(cls) -> bool:
        return cls._useSniffer

    @useSniffer.setter
    @classmethod
    def useSniffer(cls, sniffer: bool) -> None:
        cls._useSniffer = sniffer

    @classmethod
    @property
    def connectionType(cls) -> str:
        return cls._currentConnectionType

    @property
    def hasReceivedMsg(cls) -> bool:
        return cls._hasReceivedMsg

    @hasReceivedMsg.setter
    @classmethod
    def hasReceivedMsg(cls, value: bool) -> None:
        cls._hasReceivedMsg = value

    @property
    @classmethod
    def hasReceivedNetworkMsg(cls) -> bool:
        return cls._hasReceivedNetworkMsg

    @hasReceivedNetworkMsg.setter
    @classmethod
    def hasReceivedNetworkMsg(cls, value: bool) -> None:
        cls._hasReceivedNetworkMsg = value

    @classmethod
    def getConnection(cls) -> MultiConnection:
        if not cls._currentConnection:
            cls.createConnection()
        return cls._currentConnection

    @classmethod
    def connectToLoginServer(cls, host: str, port: int) -> None:
        if cls._currentConnection != None:
            cls.closeConnection()
        cls.etablishConnection(
            host, port, ConnectionType.TO_LOGIN_SERVER, cls._useSniffer
        )
        cls._currentConnectionType = ConnectionType.TO_LOGIN_SERVER

    @classmethod
    def connectToGameServer(cls, gameServerHost: str, gameServerPort: int) -> None:
        cls.startConnectionTimer()
        if cls._currentConnection != None:
            cls.closeConnection()
        cls.etablishConnection(
            gameServerHost,
            gameServerPort,
            ConnectionType.TO_GAME_SERVER,
            cls._useSniffer,
        )
        cls._currentConnectionType = ConnectionType.TO_GAME_SERVER
        PlayerManager().gameServerPort = gameServerPort

    @classmethod
    def connectToKoliServer(cls, gameServerHost: str, gameServerPort: int) -> None:
        cls.startConnectionTimer()
        if cls._currentConnection != None and cls._currentConnection.getSubConnection(
            ConnectionType.TO_KOLI_SERVER
        ):
            cls._currentConnection.close(ConnectionType.TO_KOLI_SERVER)
        cls.etablishConnection(
            gameServerHost,
            gameServerPort,
            ConnectionType.TO_KOLI_SERVER,
            cls._useSniffer,
        )
        cls._currentConnectionType = ConnectionType.TO_KOLI_SERVER
        PlayerManager().kisServerPort = gameServerPort

    @classmethod
    def confirmGameServerConnection(cls) -> None:
        cls.stopConnectionTimer()

    @classmethod
    def onConnectionTimeout(cls) -> None:
        msg: BasicPingMessage = None
        if cls._currentConnection and cls._currentConnection.connected:
            msg = BasicPingMessage()
            msg.initBasicPingMessage(True)
            logger.warn(
                "La connection au serveur de jeu semble longue. On envoit un BasicPingMessage pour essayer de débloquer la situation."
            )
            cls._currentConnection.send(msg, cls._currentConnectionType)
            cls.stopConnectionTimer()

    @classmethod
    def closeConnection(cls) -> None:
        if krnl.Kernel().getWorker().contains(HandshakeFrame):
            krnl.Kernel().getWorker().removeFrame(
                krnl.Kernel().getWorker().getFrame(HandshakeFrame)
            )
        if cls._currentConnection and cls._currentConnection.connected:
            cls._currentConnection.close()
        cls._currentConnection = None
        cls._currentConnectionType = ConnectionType.DISCONNECTED

    @classmethod
    def handleDisconnection(cls) -> DisconnectionReason:
        cls.closeConnection()
        reason: DisconnectionReason = DisconnectionReason(
            cls._wantedSocketLost, cls._wantedSocketLostReason
        )
        cls._wantedSocketLost = False
        cls._wantedSocketLostReason = DisconnectionReasonEnum.UNEXPECTED
        return reason

    @classmethod
    def connectionGonnaBeClosed(cls, expectedReason: int) -> None:
        cls._wantedSocketLostReason = expectedReason
        cls._wantedSocketLost = True

    @classmethod
    def pause(cls) -> None:
        logger.info("Pause connection")
        cls._currentConnection.pause()

    @classmethod
    def resume(cls) -> None:
        logger.info("Resume connection")
        if cls._currentConnection:
            cls._currentConnection.resume()
        krnl.Kernel().getWorker().process(ConnectionResumedMessage())

    @classmethod
    def startConnectionTimer(cls) -> None:
        if not cls._connectionTimeout:
            cls._connectionTimeout = Timer(4, cls.onConnectionTimeout)
        else:
            cls._connectionTimeout.cancel()
        cls._connectionTimeout.start()

    @classmethod
    def stopConnectionTimer(cls) -> None:
        if cls._connectionTimeout:
            cls._connectionTimeout.cancel()

    @classmethod
    def etablishConnection(
        cls,
        host: str,
        port: int,
        id: str,
        useSniffer: bool = False,
        proxy: IConnectionProxy = None,
    ) -> None:
        conn: IServerConnection = None
        if useSniffer:
            if proxy is not None:
                raise ArgumentError(
                    "Can't etablish a connection using a proxy and the sniffer."
                )
            conn = SnifferServerConnection(None, 0, id)
        elif proxy != None:
            conn = ProxyedServerConnection(proxy, None, 0, id)
        else:
            conn = ServerConnection(None, 0, id)
        if not cls._currentConnection:
            cls.createConnection()
        conn.lagometer = LagometerAck()
        conn.handler = krnl.Kernel().getWorker()
        conn.rawParser = MessageReceiver()
        cls._currentConnection.addConnection(conn, id)
        cls._currentConnection.mainConnection = conn
        krnl.Kernel().getWorker().addFrame(HandshakeFrame())
        conn.connect(host, port)

    @classmethod
    def createConnection(cls) -> None:
        cls._currentConnection = MultiConnection()

import base64
from threading import Timer
from time import perf_counter, sleep
import traceback
from types import FunctionType
from whistle import Event
from com.ankamagames.jerakine.messages.ConnectedMessage import ConnectedMessage
from com.ankamagames.jerakine.network.INetworkDataContainerMessage import (
    INetworkDataContainerMessage,
)
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.messages.common.NetworkDataContainerMessage import (
    NetworkDataContainerMessage,
)
from com.ankamagames.jerakine.events.ProgressEvent import ProgressEvent
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.MessageHandler import MessageHandler
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.ILagometer import ILagometer
from com.ankamagames.jerakine.network.IServerConnection import IServerConnection
from com.ankamagames.jerakine.network.RawDataParser import RawDataParser
from com.ankamagames.jerakine.events.SocketEvent import SocketEvent
from com.ankamagames.jerakine.events.IOErrorEvent import IOErrorEvent
from com.ankamagames.jerakine.events.SecurityErrorEvent import SecurityErrorEvent
from com.ankamagames.jerakine.network.UnpackMode import UnpackMode
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import (
    ServerConnectionFailedMessage,
)
from com.ankamagames.jerakine.network.utils.FuncTree import FuncTree
from com.ankamagames.jerakine.utils.display.EnterFrameConst import EnterFrameConst
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import (
    EnterFrameDispatcher,
)
from mx.CustomSocket.Socket import Socket
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage

logger = Logger(__name__)


class ServerConnection(IServerConnection):

    DEBUG_VERBOSE: bool = True

    LOG_ENCODED_CLIENT_MESSAGES: bool = True

    DEBUG_LOW_LEVEL_VERBOSE: bool = True

    DEBUG_DATA: bool = True

    LATENCY_AVG_BUFFER_SIZE: int = 50

    MESSAGE_SIZE_ASYNC_THRESHOLD: int = 300 * 1024

    def __init__(
        self, host: str = None, port: int = 0, id: str = "", secure: bool = False
    ):
        self._latencyBuffer = []
        self._asyncMessages = list[INetworkMessage]()
        self._asyncTrees = list[FuncTree]()
        self._input = ByteArray()
        self._socket = Socket(host, port)
        self._remoteSrvHost = host
        self._remoteSrvPort = port
        self._id = id
        self._connecting = False
        self.disabled = False
        self.disabledIn = False
        self.disabledOut = False
        self._rawParser: RawDataParser = None
        self._handler: MessageHandler = None
        self._outputBuffer = list[INetworkMessage]()
        self._splittedPacket = False
        self._staticHeader: int = -1
        self._splittedPacketId: int = -1
        self._splittedPacketLength: int = -1
        self._inputBuffer = ByteArray()
        self._pauseBuffer = list()
        self._pause: bool = False
        self._latestSent: int = 0
        self._lastSent: int = None
        self._lagometer: ILagometer = None
        self._sendSequenceId: int = 0
        self._asyncNetworkDataContainerMessage: NetworkDataContainerMessage = None
        self._willClose: bool = None
        self._maxUnpackTime: int = float("inf")
        self._firstConnectionTry: bool = True
        super().__init__()

    def close(self) -> None:
        if self._socket.connected:
            logger.debug(f"[{self._id}] Closing socket for connection! ")
            EnterFrameDispatcher().removeEventListener(self.onEnterFrame)
            self._socket.close()
        elif not self.checkClosed():
            logger.warn(
                f"[{self._id}] Tried to close a socket while it had already been disconnected."
            )
            EnterFrameDispatcher().removeEventListener(self.onEnterFrame)

    @property
    def rawParser(self) -> RawDataParser:
        return self._rawParser

    @rawParser.setter
    def rawParser(self, value: RawDataParser) -> None:
        self._rawParser = value

    @property
    def handler(self) -> MessageHandler:
        return self._handler

    @handler.setter
    def handler(self, value: MessageHandler) -> None:
        self._handler = value

    @property
    def pauseBuffer(self) -> list:
        return self._pauseBuffer

    @property
    def latencyAvg(self) -> int:
        latency: int = 0
        if len(self._latencyBuffer) == 0:
            return 0
        total: int = 0
        for latency in self._latencyBuffer:
            total += latency
        return total / len(self._latencyBuffer)

    @property
    def latencySamplesCount(self) -> int:
        return len(self._latencyBuffer)

    @property
    def latencySamplesMax(self) -> int:
        return self.LATENCY_AVG_BUFFER_SIZE

    @property
    def port(self) -> int:
        return self._remoteSrvPort

    @property
    def lastSent(self) -> int:
        return self._lastSent

    @property
    def lagometer(self) -> ILagometer:
        return self._lagometer

    @lagometer.setter
    def lagometer(self, l: ILagometer) -> None:
        self._lagometer = l

    @property
    def sendSequenceId(self) -> int:
        return self._sendSequenceId

    @property
    def connected(self) -> bool:
        return self._socket.connected

    @property
    def connecting(self) -> bool:
        return self._connecting

    def connect(self, host: str, port: int) -> None:
        if self._connecting or self.disabled or self.disabledIn and self.disabledOut:
            return
        self._connecting = True
        self._firstConnectionTry = True
        self._remoteSrvHost = host
        self._remoteSrvPort = port
        self.addListeners()
        logger.info(f"[{self._id}] Connecting to {host}:{port}...")
        self._timeoutTimer = Timer(interval=7, function=self.onSocketTimeOut)
        self._timeoutTimer.start()
        try:
            self._socket.connect(host, port)
        except Exception as e:
            logger.error(
                "["
                + str(self._id)
                + "] Could not establish connection to the serveur!\n",
                exc_info=True,
            )

    def getType(self, v) -> str:
        className: str = v.__class__.__name__
        if className.find("list") != -1:
            className = className.split("list[").join("list{")
            className = className.split("]").join("}")
        else:
            className = className.split(".").pop()
        if isinstance(v, INetworkMessage):
            className += ", id: " + v.getMessageId()
        return className

    def send(self, msg: INetworkMessage, connectionId: str = "") -> None:
        if self.DEBUG_DATA:
            logger.debug(
                f"[{self._id}] [SND] > {msg.__class__.__name__ if self.DEBUG_VERBOSE else msg}"
            )
        if self.disabled or self.disabledOut:
            return
        if not self._socket.connected:
            if self._connecting:
                if not self._outputBuffer:
                    self._outputBuffer = []
                self._outputBuffer.append(msg)
            return
        self.lowSend(msg)

    def __str__(self) -> str:
        status = "Server connection status:\n"
        status += (
            "  Connected:       " + ("Yes" if self._socket.connected else "No") + "\n"
        )
        if self._socket.connected:
            status += (
                "  Connected to:    "
                + self._remoteSrvHost
                + ":"
                + self._remoteSrvPort
                + "\n"
            )
        else:
            status += (
                "  Connecting:      " + ("Yes" if self._connecting else "No") + "\n"
            )
        if self._connecting:
            status += (
                "  Connecting to:   "
                + self._remoteSrvHost
                + ":"
                + self._remoteSrvPort
                + "\n"
            )
        status += "  Raw parser:      " + self.rawParser + "\n"
        status += "  Message handler: " + self.handler + "\n"
        if self._outputBuffer:
            status += "  Output buffer:   " + len(self._outputBuffer) + " message(s)\n"
        if self._inputBuffer:
            status += "  Input buffer:    " + len(self._inputBuffer) + " byte(s)\n"
        if self._splittedPacket:
            status += "  Splitted message in the input buffer:\n"
            status += "    Message ID:      " + self._splittedPacketId + "\n"
            status += "    Awaited length:  " + self._splittedPacketLength + "\n"
        return status

    def pause(self) -> None:
        self._pause = True

    def resume(self) -> None:
        self._pause = False
        while len(self._pauseBuffer) and not self._pause:
            msg = self._pauseBuffer.pop(0)
            if self.DEBUG_DATA:
                logger.debug(
                    "["
                    + str(self._id)
                    + "] [RCV] (after Resume) "
                    + msg.__class__.__name__
                )
            self._handler.process(msg)
        self._pauseBuffer = []

    def stopConnectionTimeout(self) -> None:
        if self._timeoutTimer:
            self._timeoutTimer.cancel()
            self._timeoutTimer = None

    def addEventListener(
        self,
        type: str,
        listener: FunctionType,
        useCapture: bool = False,
        priority: int = 0,
        useWeakReference: bool = False,
    ) -> None:
        self._socket.addEventListener(
            type, listener, useCapture, priority, useWeakReference
        )

    def dispatchEvent(self, event: Event) -> bool:
        return self._socket.dispatchEvent(event)

    def hasEventListener(self, type: str) -> bool:
        return self._socket.hasEventListener(type)

    def removeEventListener(
        self, type: str, listener: FunctionType, useCapture: bool = False
    ) -> None:
        self._socket.removeEventListener(type, listener, useCapture)

    def willTrigger(self, type: str) -> bool:
        return self._socket.willTrigger(type)

    def ConnectingOnAnotherPort(self, port: int) -> None:
        self.connect(self._remoteSrvHost, port)

    def addListeners(self) -> None:
        self._socket.addEventListener(ProgressEvent.SOCKET_DATA, self.onSocketData, 0)
        self._socket.addEventListener(SocketEvent.CONNECT, self.onConnect, 0)
        self._socket.addEventListener(SocketEvent.CLOSE, self.onClose, float("inf"))
        self._socket.addEventListener(IOErrorEvent.IO_ERROR, self.onSocketError, 0)
        EnterFrameDispatcher().addEventListener(
            self.onEnterFrame, EnterFrameConst.SERVER_CONNECTION
        )

    def removeListeners(self) -> None:
        self._socket.removeEventListener(ProgressEvent.SOCKET_DATA, self.onSocketData)
        self._socket.removeEventListener(SocketEvent.CONNECT, self.onConnect)
        self._socket.removeEventListener(SocketEvent.CLOSE, self.onClose)
        self._socket.removeEventListener(IOErrorEvent.IO_ERROR, self.onSocketError)
        EnterFrameDispatcher().removeEventListener(self.onEnterFrame)

    def receive(self, input: ByteArray, fromEnterFrame: bool = False) -> None:
        try:
            if input.remaining() > 0:
                if self.DEBUG_LOW_LEVEL_VERBOSE:
                    if fromEnterFrame:
                        logger.info(
                            f"[{self._id}] Handling data, byte available : {input.remaining()}  trigger by a timer"
                        )
                    else:
                        logger.info(
                            f"[{self._id}] Handling data, byte available : {input.remaining()}"
                        )
                msg: NetworkMessage = self.lowReceive(input)
                while msg is not None:
                    if self._lagometer:
                        self._lagometer.pong(msg)
                    msg.receptionTime = perf_counter()
                    msg.sourceConnection = self._id
                    self.process(msg)
                    if (
                        self._asyncNetworkDataContainerMessage != None
                        and self._asyncNetworkDataContainerMessage.content.remaining()
                    ):
                        msg = self.lowReceive(
                            self._asyncNetworkDataContainerMessage.content
                        )
                    else:
                        if self.checkClosed() and not self._socket.connected:
                            break
                        if input.remaining() <= 0:
                            break
                        msg = self.lowReceive(input)
        except Exception as e:
            logger.error(
                "[" + str(self._id) + "] Error while reading socket. \n", exc_info=True
            )
            self.close()

    def checkClosed(self) -> bool:
        if self._willClose:
            if len(self._asyncTrees) == 0:
                self._willClose = False
                self.dispatchEvent(SocketEvent.CLOSE)
            return True
        return False

    def process(self, msg: INetworkMessage) -> None:
        if msg.unpacked:
            if isinstance(msg, INetworkDataContainerMessage):
                self._asyncNetworkDataContainerMessage = msg
            elif not self._pause:
                if (
                    self.DEBUG_DATA
                    and msg.getMessageId() != 176
                    and msg.getMessageId() != 6362
                ):
                    logger.debug(f"[{self._id}] [RCV] " + msg.__class__.__name__)
                if not self.disabledIn:
                    self._handler.process(msg)
            else:
                self._pauseBuffer.append(msg)

    def getMessageId(self, firstOctet: int) -> int:
        return firstOctet >> NetworkMessage.BIT_RIGHT_SHIFT_LEN_PACKET_ID

    def readMessageLength(self, staticHeader: int, src: ByteArray) -> int:
        byteLenDynamicHeader: int = staticHeader & NetworkMessage.BIT_MASK
        messageLength: int = int.from_bytes(src.read(byteLenDynamicHeader), "big")
        return messageLength

    def lowSend(self, msg: NetworkMessage) -> None:
        if self.LOG_ENCODED_CLIENT_MESSAGES and msg.getMessageId() not in [
            5607,
            6372,
            6156,
            6609,
            4,
            6119,
            110,
            6540,
            6648,
            6608,
        ]:
            data = msg.pack()
            logger.debug(
                "[{self._id}] [SND] > {msg} ---" + str(base64.encodebytes(data)) + "---"
            )
        self._socket.send(msg.pack())
        self._latestSent = perf_counter()
        self._lastSent = perf_counter()
        self._sendSequenceId += 1
        if self._lagometer:
            self._lagometer.ping(msg)

    def lowReceive(self, src: ByteArray) -> NetworkMessage:
        if self.DEBUG_LOW_LEVEL_VERBOSE and self._splittedPacket:
            logger.debug(
                f"Gathering splited packet of length {self._splittedPacketLength},"
                f"already received {len(self._inputBuffer)}, remaining {self._splittedPacketLength - len(self._inputBuffer)}. I just received {src.remaining()}"
            )
        messageLength = 0

        if not self._splittedPacket:

            if src.remaining() < 2:
                if self.DEBUG_LOW_LEVEL_VERBOSE:
                    logger.info(
                        f"[{self._id}] Not enough data to read the header, byte available : {src.remaining()} (needed : 2)"
                    )
                return None

            staticHeader = src.readUnsignedShort()
            messageId = self.getMessageId(staticHeader)
            if messageId not in self._rawParser._messagesTypes:
                raise Exception(f"Unknown message id {messageId}")
            byteLenDynamicHeader = staticHeader & NetworkMessage.BIT_MASK

            if src.remaining() >= byteLenDynamicHeader:
                messageLength = self.readMessageLength(staticHeader, src)

                if src.remaining() >= messageLength:
                    self.updateLatency()

                    if self.getUnpackMode(messageId, messageLength) == UnpackMode.ASYNC:
                        self._input = src.read(messageLength)
                        msg = self._rawParser.parseAsync(
                            self._input, messageId, messageLength, self.computeMessage
                        )
                        if self.DEBUG_LOW_LEVEL_VERBOSE and msg != None:
                            logger.info(
                                f"[{self._id}] Async {self.getType(msg)} parsing, message length : {messageLength})"
                            )

                    else:
                        msg = self._rawParser.parse(src, messageId, messageLength)
                        if self.DEBUG_LOW_LEVEL_VERBOSE:
                            logger.info(f"[{self._id}] Full parsing done")
                    return msg

                if self.DEBUG_LOW_LEVEL_VERBOSE:
                    logger.info(
                        f"[{self._id}] Not enough data to read msg content, byte available : {src.remaining()} (needed : {messageLength} bytes)"
                    )

                self._staticHeader = -1
                self._splittedPacketLength = messageLength
                self._splittedPacketId = messageId
                self._splittedPacket = True
                self._inputBuffer = src.read(src.remaining())

                return None

            if self.DEBUG_LOW_LEVEL_VERBOSE:
                logger.info(
                    f"[{self._id}] Not enough data to read message ID, byte available : {src.remaining()}  (needed :  {staticHeader & NetworkMessage.BIT_MASK} )"
                )

            self._staticHeader = staticHeader
            self._splittedPacketLength = messageLength
            self._splittedPacketId = messageId
            self._splittedPacket = True
            return None

        if self._staticHeader != -1:
            self._splittedPacketLength = self.readMessageLength(self._staticHeader, src)
            self._staticHeader = -1

        if src.remaining() + len(self._inputBuffer) >= self._splittedPacketLength:
            self._inputBuffer = self._inputBuffer + src.read(
                self._splittedPacketLength - len(self._inputBuffer)
            )
            self._inputBuffer.position = 0
            self.updateLatency()

            if (
                self.getUnpackMode(self._splittedPacketId, self._splittedPacketLength)
                == UnpackMode.ASYNC
            ):
                msg = self._rawParser.parseAsync(
                    self._inputBuffer,
                    self._splittedPacketId,
                    self._splittedPacketLength,
                    self.computeMessage,
                )
                if self.DEBUG_LOW_LEVEL_VERBOSE and msg != None:
                    logger.info(
                        f"[{self._id}] Async splitted {self.getType(msg)} parsing, message length : {self._splittedPacketLength})"
                    )
            else:
                msg = self._rawParser.parse(
                    self._inputBuffer,
                    self._splittedPacketId,
                    self._splittedPacketLength,
                )
                if self.DEBUG_LOW_LEVEL_VERBOSE:
                    logger.info(f"[{self._id}] Full parsing done")

            self._splittedPacket = False
            self._inputBuffer = ByteArray()
            return msg

        self._inputBuffer += src.read(src.remaining())
        return None

    def getUnpackMode(self, messageId: int, messageLength: int) -> int:
        if messageLength == 0:
            return UnpackMode.SYNC
        result: int = self._rawParser.getUnpackMode(messageId)
        if result != UnpackMode.DEFAULT:
            return result
        if messageLength > self.MESSAGE_SIZE_ASYNC_THRESHOLD:
            result = UnpackMode.ASYNC
            logger.info(
                f"Handling too heavy message of id {messageId} asynchronously (size : {messageLength})"
            )
        else:
            result = UnpackMode.SYNC
        return result

    def computeMessage(self, msg: INetworkMessage, tree: FuncTree) -> None:
        if not tree.goDown():
            msg.unpacked = True
            return
        self._asyncMessages.append(msg)
        self._asyncTrees.append(tree)
        EnterFrameDispatcher().addEventListener(
            self.onEnterFrame, EnterFrameConst.SERVER_CONNECTION
        )

    def onEnterFrame(self) -> None:
        start = perf_counter()
        if self._socket.connected:
            self.receive(self._socket.buff, True)
        if len(self._asyncMessages) and len(self._asyncTrees):
            while True:
                if not self._asyncTrees[0].next():
                    if self.DEBUG_LOW_LEVEL_VERBOSE:
                        logger.info(
                            f"[{self._id}] Async {self.getType(self._asyncMessages[0])} parsing complete"
                        )
                    self._asyncTrees.pop(0)
                    self._asyncMessages[0].unpacked = True
                    self.process(self._asyncMessages.pop(0))
                    if len(self._asyncTrees) == 0:
                        EnterFrameDispatcher().removeEventListener(self.onEnterFrame)
                        return
                if perf_counter() - start < self._maxUnpackTime:
                    break

    def updateLatency(self) -> None:
        if self._pause or len(self._pauseBuffer) > 0 or self._latestSent == 0:
            return
        packetReceived: int = perf_counter()
        latency: int = packetReceived - self._latestSent
        self._latestSent = 0
        self._latencyBuffer.append(latency)
        if len(self._latencyBuffer) > self.LATENCY_AVG_BUFFER_SIZE:
            self._latencyBuffer.pop(0)

    def onConnect(self, e: Event) -> None:
        self._connecting = False
        self.stopConnectionTimeout()
        if self.DEBUG_DATA:
            logger.debug(f"[{self._id}] Connection opened.")
        for msg in self._outputBuffer:
            self.lowSend(msg)
        self._inputBuffer = ByteArray()
        self._outputBuffer = []
        if self._handler:
            self._handler.process(ConnectedMessage())

    def onClose(self, e: Event) -> None:
        if len(self._asyncMessages) != 0:
            e.stopImmediatePropagation()
            self._willClose = True
            return
        if self.DEBUG_DATA:
            logger.debug("[" + str(self._id) + "] Connection closed.")
        Timer(3, self.removeListeners).start()
        if self._lagometer:
            self._lagometer.stop()
        from com.ankamagames.jerakine.network.ServerConnectionClosedMessage import (
            ServerConnectionClosedMessage,
        )

        self._handler.process(ServerConnectionClosedMessage(self))
        self._connecting = False
        self._outputBuffer = []
        EnterFrameDispatcher().removeEventListener(self.onEnterFrame)
        self._asyncTrees = list[FuncTree]()
        self._asyncMessages = list[INetworkMessage]()
        self._asyncNetworkDataContainerMessage = None
        self._input = ByteArray()
        self._splittedPacket = False
        self._staticHeader = -1

    def onSocketData(self, pe: ProgressEvent) -> None:
        if self.DEBUG_LOW_LEVEL_VERBOSE:
            logger.info(
                f"[{self._id}] Receive Event, byte available : {self._socket.buff.remaining()}"
            )
        self.receive(self._socket.buff)

    def onSocketError(self, e: IOErrorEvent) -> None:
        if self._lagometer:
            self._lagometer.stop()
        logger.error("[" + str(self._id) + "] Failure while opening socket.")
        self._connecting = False
        self._handler.process(ServerConnectionFailedMessage(self, e.text))

    def onSocketTimeOut(self) -> None:
        if self._lagometer:
            self._lagometer.stop()
        self._connecting = False
        if self._firstConnectionTry:
            logger.error(
                "["
                + str(self._id)
                + "] Failure while opening socket, timeout, but WWJD ? Give a second chance !"
            )
            self.connect(self._remoteSrvHost, self._remoteSrvPort)
            self._firstConnectionTry = False
        else:
            logger.error(
                "[" + str(self._id) + "] Failure while opening socket, timeout."
            )
            self._handler.process(ServerConnectionFailedMessage(self, "timeout"))

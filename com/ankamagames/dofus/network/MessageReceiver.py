import importlib
import json
import sys
from types import FunctionType
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.jerakine.network.RawDataParser import RawDataParser
from com.ankamagames.jerakine.network.UnpackMode import UnpackMode
import com.ankamagames.dofus.Constants as Constants

logger = Logger(__name__)
with open(Constants.PROTOCOL_MSG_SHUFFLE_PATH, "r") as fp:
    msgShuffle = json.load(fp)


class MessageReceiver(RawDataParser):
    logger = Logger(__name__)
    _messagesTypes: dict = dict()
    _unpackModes: dict = dict()
    for cls_name, cls_infos in msgShuffle.items():
        modulePath = cls_infos["module"]
        try:
            clsModule = sys.modules[modulePath]
        except:
            clsModule = importlib.import_module(modulePath)
        cls = getattr(clsModule, cls_name)
        _messagesTypes[cls_infos["id"]] = cls
    _unpackModes[2516] = UnpackMode.ASYNC

    def __init__(self):
        super().__init__()

    def register(self) -> None:
        for cls in self._messagesTypes.values():
            StoreDataManager().registerClass(cls(), True, True)

    def parse(
        self, input: ByteArray, messageId: int, messageLength: int
    ) -> INetworkMessage:
        messageType: NetworkMessage = self._messagesTypes[messageId]
        if not messageType:
            logger.warn(
                f"Unknown packet received (ID {messageId}  , length {messageLength}"
            )
            return None
        message = messageType.unpack(input, messageLength)
        message.unpacked = True
        return message

    def parseAsync(
        self,
        input: ByteArray,
        messageId: int,
        messageLength: int,
        callback: FunctionType,
    ) -> INetworkMessage:
        messageType = self._messagesTypes[messageId]
        if not messageType:
            logger.warn(
                "Unknown packet received (ID "
                + messageId
                + ", length "
                + messageLength
                + ")"
            )
            return None
        message: INetworkMessage = messageType()
        message.unpacked = False
        callback(message, message.unpackAsync(input, messageLength))
        return message

    def getUnpackMode(self, messageId: int) -> int:
        return (
            self._unpackModes[messageId]
            if messageId in self._unpackModes
            else UnpackMode.DEFAULT
        )

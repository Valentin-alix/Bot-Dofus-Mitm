from types import FunctionType
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class RawDataParser:
    _messagesTypes = dict()

    def parse(self, data: ByteArray, msgId: int, msgLen: int) -> INetworkMessage:
        pass

    def parseAsync(
        self, data: ByteArray, messageId: int, msgLen: int, compute: FunctionType
    ) -> INetworkMessage:
        pass

    def getUnpackMode(self, param1: int) -> int:
        pass

from com.ankamagames.jerakine.messages.QueueableMessage import QueueableMessage
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.IdentifiedMessage import IdentifiedMessage
from com.ankamagames.jerakine.network.utils.FuncTree import FuncTree


class INetworkMessage(IdentifiedMessage, QueueableMessage):
    def pack(self, param1: ByteArray) -> None:
        pass

    def unpack(self, param1: ByteArray, param2: int) -> None:
        pass

    def unpackAsync(self, param1: ByteArray, param2: int) -> FuncTree:
        pass

    @property
    def isInitialized(self) -> bool:
        pass

    @property
    def unpacked(self) -> bool:
        pass

    @unpacked.setter
    def unpacked(self, param1: bool) -> None:
        pass

from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IConnectionProxy:
    def processAndSend(self, param1: INetworkMessage, param2: ByteArray) -> None:
        pass

    def processAndReceive(self, param1: ByteArray) -> INetworkMessage:
        pass

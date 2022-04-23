from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IMessageRouter:
    def getConnectionId(param1: INetworkMessage) -> str:
        pass

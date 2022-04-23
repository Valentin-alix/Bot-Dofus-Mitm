from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ILagometer:
    def ping(self, param1: INetworkMessage = None) -> None:
        pass

    def pong(self, param1: INetworkMessage = None) -> None:
        pass

    def stop(self) -> None:
        pass

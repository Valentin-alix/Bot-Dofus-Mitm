from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsPaddockRemoveMessage(NetworkMessage):
    mountsId:list[int]
    

    def init(self, mountsId_:list[int]):
        self.mountsId = mountsId_
        
        super().__init__()
    
    
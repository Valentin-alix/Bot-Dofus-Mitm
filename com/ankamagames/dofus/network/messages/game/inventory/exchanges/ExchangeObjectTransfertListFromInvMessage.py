from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListFromInvMessage(NetworkMessage):
    ids:list[int]
    

    def init(self, ids_:list[int]):
        self.ids = ids_
        
        super().__init__()
    
    
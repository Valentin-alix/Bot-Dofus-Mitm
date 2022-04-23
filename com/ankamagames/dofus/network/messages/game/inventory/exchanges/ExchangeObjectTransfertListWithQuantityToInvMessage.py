from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    ids:list[int]
    qtys:list[int]
    

    def init(self, ids_:list[int], qtys_:list[int]):
        self.ids = ids_
        self.qtys = qtys_
        
        super().__init__()
    
    
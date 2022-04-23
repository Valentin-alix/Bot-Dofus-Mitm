from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcTradeMessage(NetworkMessage):
    npcId:int
    

    def init(self, npcId_:int):
        self.npcId = npcId_
        
        super().__init__()
    
    
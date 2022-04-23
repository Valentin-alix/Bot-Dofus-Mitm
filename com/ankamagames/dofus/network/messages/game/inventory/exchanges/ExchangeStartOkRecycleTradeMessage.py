from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkRecycleTradeMessage(NetworkMessage):
    percentToPrism:int
    percentToPlayer:int
    

    def init(self, percentToPrism_:int, percentToPlayer_:int):
        self.percentToPrism = percentToPrism_
        self.percentToPlayer = percentToPlayer_
        
        super().__init__()
    
    
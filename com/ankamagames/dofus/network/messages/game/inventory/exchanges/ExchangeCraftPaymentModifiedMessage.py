from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModifiedMessage(NetworkMessage):
    goldSum:int
    

    def init(self, goldSum_:int):
        self.goldSum = goldSum_
        
        super().__init__()
    
    
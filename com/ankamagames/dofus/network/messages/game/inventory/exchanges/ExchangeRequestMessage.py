from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeRequestMessage(NetworkMessage):
    exchangeType:int
    

    def init(self, exchangeType_:int):
        self.exchangeType = exchangeType_
        
        super().__init__()
    
    
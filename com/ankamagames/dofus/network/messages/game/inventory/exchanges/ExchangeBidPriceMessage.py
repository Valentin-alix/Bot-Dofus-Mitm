from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidPriceMessage(NetworkMessage):
    genericId:int
    averagePrice:int
    

    def init(self, genericId_:int, averagePrice_:int):
        self.genericId = genericId_
        self.averagePrice = averagePrice_
        
        super().__init__()
    
    
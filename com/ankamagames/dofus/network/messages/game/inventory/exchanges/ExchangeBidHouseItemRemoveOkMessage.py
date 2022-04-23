from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(NetworkMessage):
    sellerId:int
    

    def init(self, sellerId_:int):
        self.sellerId = sellerId_
        
        super().__init__()
    
    
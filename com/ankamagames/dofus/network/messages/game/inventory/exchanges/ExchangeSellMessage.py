from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeSellMessage(NetworkMessage):
    objectToSellId:int
    quantity:int
    

    def init(self, objectToSellId_:int, quantity_:int):
        self.objectToSellId = objectToSellId_
        self.quantity = quantity_
        
        super().__init__()
    
    
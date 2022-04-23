from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBuyMessage(NetworkMessage):
    objectToBuyId:int
    quantity:int
    

    def init(self, objectToBuyId_:int, quantity_:int):
        self.objectToBuyId = objectToBuyId_
        self.quantity = quantity_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeShopStockMovementRemovedMessage(NetworkMessage):
    objectId:int
    

    def init(self, objectId_:int):
        self.objectId = objectId_
        
        super().__init__()
    
    
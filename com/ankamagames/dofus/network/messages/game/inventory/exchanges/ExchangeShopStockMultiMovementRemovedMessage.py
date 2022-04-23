from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(NetworkMessage):
    objectIdList:list[int]
    

    def init(self, objectIdList_:list[int]):
        self.objectIdList = objectIdList_
        
        super().__init__()
    
    
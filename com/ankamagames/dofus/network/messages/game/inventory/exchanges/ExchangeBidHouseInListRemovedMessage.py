from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    itemUID:int
    objectGID:int
    objectType:int
    

    def init(self, itemUID_:int, objectGID_:int, objectType_:int):
        self.itemUID = itemUID_
        self.objectGID = objectGID_
        self.objectType = objectType_
        
        super().__init__()
    
    
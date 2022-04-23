from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(NetworkMessage):
    objGenericId:int
    

    def init(self, objGenericId_:int):
        self.objGenericId = objGenericId_
        
        super().__init__()
    
    
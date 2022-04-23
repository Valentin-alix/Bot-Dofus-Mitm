from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHousePriceMessage(NetworkMessage):
    objectGID:int
    

    def init(self, objectGID_:int):
        self.objectGID = objectGID_
        
        super().__init__()
    
    
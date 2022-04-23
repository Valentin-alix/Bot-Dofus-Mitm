from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObtainedItemMessage(NetworkMessage):
    genericId:int
    baseQuantity:int
    

    def init(self, genericId_:int, baseQuantity_:int):
        self.genericId = genericId_
        self.baseQuantity = baseQuantity_
        
        super().__init__()
    
    
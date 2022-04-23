from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccessoryPreviewRequestMessage(NetworkMessage):
    genericId:list[int]
    

    def init(self, genericId_:list[int]):
        self.genericId = genericId_
        
        super().__init__()
    
    
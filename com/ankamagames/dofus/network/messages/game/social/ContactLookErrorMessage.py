from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ContactLookErrorMessage(NetworkMessage):
    requestId:int
    

    def init(self, requestId_:int):
        self.requestId = requestId_
        
        super().__init__()
    
    
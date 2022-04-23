from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ContactLookRequestMessage(NetworkMessage):
    requestId:int
    contactType:int
    

    def init(self, requestId_:int, contactType_:int):
        self.requestId = requestId_
        self.contactType = contactType_
        
        super().__init__()
    
    
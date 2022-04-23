from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    

    def init(self, msgId_:int, timeStamp_:int, owner_:str, objectGenericId_:int):
        self.msgId = msgId_
        self.timeStamp = timeStamp_
        self.owner = owner_
        self.objectGenericId = objectGenericId_
        
        super().__init__()
    
    
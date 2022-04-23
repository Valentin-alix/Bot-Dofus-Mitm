from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    msgId:int
    parameters:list[str]
    livingObject:int
    

    def init(self, msgId_:int, parameters_:list[str], livingObject_:int):
        self.msgId = msgId_
        self.parameters = parameters_
        self.livingObject = livingObject_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TextInformationMessage(NetworkMessage):
    msgType:int
    msgId:int
    parameters:list[str]
    

    def init(self, msgType_:int, msgId_:int, parameters_:list[str]):
        self.msgType = msgType_
        self.msgId = msgId_
        self.parameters = parameters_
        
        super().__init__()
    
    
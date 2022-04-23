from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SystemMessageDisplayMessage(NetworkMessage):
    hangUp:bool
    msgId:int
    parameters:list[str]
    

    def init(self, hangUp_:bool, msgId_:int, parameters_:list[str]):
        self.hangUp = hangUp_
        self.msgId = msgId_
        self.parameters = parameters_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebugInClientMessage(NetworkMessage):
    level:int
    message:str
    

    def init(self, level_:int, message_:str):
        self.level = level_
        self.message = message_
        
        super().__init__()
    
    
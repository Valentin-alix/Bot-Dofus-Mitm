from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ConsoleMessage(NetworkMessage):
    type:int
    content:str
    

    def init(self, type_:int, content_:str):
        self.type = type_
        self.content = content_
        
        super().__init__()
    
    
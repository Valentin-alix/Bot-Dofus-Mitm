from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AdminCommandMessage(NetworkMessage):
    content:str
    

    def init(self, content_:str):
        self.content = content_
        
        super().__init__()
    
    
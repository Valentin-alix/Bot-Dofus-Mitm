from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PlayerNote(NetworkMessage):
    content:str
    lastEditDate:int
    

    def init(self, content_:str, lastEditDate_:int):
        self.content = content_
        self.lastEditDate = lastEditDate_
        
        super().__init__()
    
    
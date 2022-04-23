from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    lockDuration:int
    author:str
    content:str
    

    def init(self, lockDuration_:int, author_:str, content_:str):
        self.lockDuration = lockDuration_
        self.author = author_
        self.content = content_
        
        super().__init__()
    
    
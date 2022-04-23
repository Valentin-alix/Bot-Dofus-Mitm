from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitleLostMessage(NetworkMessage):
    titleId:int
    

    def init(self, titleId_:int):
        self.titleId = titleId_
        
        super().__init__()
    
    
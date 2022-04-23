from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitleSelectRequestMessage(NetworkMessage):
    titleId:int
    

    def init(self, titleId_:int):
        self.titleId = titleId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CinematicMessage(NetworkMessage):
    cinematicId:int
    

    def init(self, cinematicId_:int):
        self.cinematicId = cinematicId_
        
        super().__init__()
    
    
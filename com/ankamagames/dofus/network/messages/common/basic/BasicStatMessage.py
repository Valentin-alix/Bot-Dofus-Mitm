from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicStatMessage(NetworkMessage):
    timeSpent:int
    statId:int
    

    def init(self, timeSpent_:int, statId_:int):
        self.timeSpent = timeSpent_
        self.statId = statId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LifePointsRegenBeginMessage(NetworkMessage):
    regenRate:int
    

    def init(self, regenRate_:int):
        self.regenRate = regenRate_
        
        super().__init__()
    
    
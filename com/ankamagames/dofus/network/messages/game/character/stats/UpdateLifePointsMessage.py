from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateLifePointsMessage(NetworkMessage):
    lifePoints:int
    maxLifePoints:int
    

    def init(self, lifePoints_:int, maxLifePoints_:int):
        self.lifePoints = lifePoints_
        self.maxLifePoints = maxLifePoints_
        
        super().__init__()
    
    
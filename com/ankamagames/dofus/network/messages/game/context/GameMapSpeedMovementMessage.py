from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapSpeedMovementMessage(NetworkMessage):
    speedMultiplier:int
    

    def init(self, speedMultiplier_:int):
        self.speedMultiplier = speedMultiplier_
        
        super().__init__()
    
    
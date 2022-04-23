from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapChangeOrientationRequestMessage(NetworkMessage):
    direction:int
    

    def init(self, direction_:int):
        self.direction = direction_
        
        super().__init__()
    
    
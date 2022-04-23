from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapNoMovementMessage(NetworkMessage):
    cellX:int
    cellY:int
    

    def init(self, cellX_:int, cellY_:int):
        self.cellX = cellX_
        self.cellY = cellY_
        
        super().__init__()
    
    
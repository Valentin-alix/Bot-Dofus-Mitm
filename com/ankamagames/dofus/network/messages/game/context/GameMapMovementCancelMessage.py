from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementCancelMessage(NetworkMessage):
    cellId:int
    

    def init(self, cellId_:int):
        self.cellId = cellId_
        
        super().__init__()
    
    
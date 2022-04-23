from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityDispositionInformations(NetworkMessage):
    cellId:int
    direction:int
    

    def init(self, cellId_:int, direction_:int):
        self.cellId = cellId_
        self.direction = direction_
        
        super().__init__()
    
    
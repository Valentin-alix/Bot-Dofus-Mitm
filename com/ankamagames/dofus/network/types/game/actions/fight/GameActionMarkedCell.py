from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionMarkedCell(NetworkMessage):
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    

    def init(self, cellId_:int, zoneSize_:int, cellColor_:int, cellsType_:int):
        self.cellId = cellId_
        self.zoneSize = zoneSize_
        self.cellColor = cellColor_
        self.cellsType = cellsType_
        
        super().__init__()
    
    
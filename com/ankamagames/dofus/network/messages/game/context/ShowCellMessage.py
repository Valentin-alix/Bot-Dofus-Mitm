from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShowCellMessage(NetworkMessage):
    sourceId:int
    cellId:int
    

    def init(self, sourceId_:int, cellId_:int):
        self.sourceId = sourceId_
        self.cellId = cellId_
        
        super().__init__()
    
    
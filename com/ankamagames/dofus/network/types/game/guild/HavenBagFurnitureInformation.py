from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagFurnitureInformation(NetworkMessage):
    cellId:int
    funitureId:int
    orientation:int
    

    def init(self, cellId_:int, funitureId_:int, orientation_:int):
        self.cellId = cellId_
        self.funitureId = funitureId_
        self.orientation = orientation_
        
        super().__init__()
    
    
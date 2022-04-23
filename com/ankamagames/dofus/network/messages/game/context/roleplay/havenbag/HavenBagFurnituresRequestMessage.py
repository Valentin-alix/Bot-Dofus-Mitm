from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    cellIds:list[int]
    funitureIds:list[int]
    orientations:list[int]
    

    def init(self, cellIds_:list[int], funitureIds_:list[int], orientations_:list[int]):
        self.cellIds = cellIds_
        self.funitureIds = funitureIds_
        self.orientations = orientations_
        
        super().__init__()
    
    
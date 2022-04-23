from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseInformations(NetworkMessage):
    houseId:int
    modelId:int
    

    def init(self, houseId_:int, modelId_:int):
        self.houseId = houseId_
        self.modelId = modelId_
        
        super().__init__()
    
    
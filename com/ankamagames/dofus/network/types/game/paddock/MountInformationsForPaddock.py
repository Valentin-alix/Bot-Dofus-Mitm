from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationsForPaddock(NetworkMessage):
    modelId:int
    name:str
    ownerName:str
    

    def init(self, modelId_:int, name_:str, ownerName_:str):
        self.modelId = modelId_
        self.name = name_
        self.ownerName = ownerName_
        
        super().__init__()
    
    
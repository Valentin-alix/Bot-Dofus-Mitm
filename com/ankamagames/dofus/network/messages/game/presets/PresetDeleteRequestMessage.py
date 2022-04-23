from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetDeleteRequestMessage(NetworkMessage):
    presetId:int
    

    def init(self, presetId_:int):
        self.presetId = presetId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetUseRequestMessage(NetworkMessage):
    presetId:int
    

    def init(self, presetId_:int):
        self.presetId = presetId_
        
        super().__init__()
    
    
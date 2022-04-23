from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PresetSaveErrorMessage(NetworkMessage):
    presetId:int
    code:int
    

    def init(self, presetId_:int, code_:int):
        self.presetId = presetId_
        self.code = code_
        
        super().__init__()
    
    
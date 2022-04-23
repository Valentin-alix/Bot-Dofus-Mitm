from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IconPresetSaveRequestMessage(NetworkMessage):
    presetId:int
    symbolId:int
    updateData:bool
    

    def init(self, presetId_:int, symbolId_:int, updateData_:bool):
        self.presetId = presetId_
        self.symbolId = symbolId_
        self.updateData = updateData_
        
        super().__init__()
    
    
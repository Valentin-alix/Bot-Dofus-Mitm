from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IdolsPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    

    def init(self, presetId_:int, symbolId_:int, updateData_:bool):
        
        super().__init__(presetId_, symbolId_, updateData_)
    
    
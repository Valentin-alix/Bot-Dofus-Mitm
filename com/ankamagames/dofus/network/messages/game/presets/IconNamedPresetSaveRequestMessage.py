from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    name:str
    type:int
    

    def init(self, name_:str, type_:int, presetId_:int, symbolId_:int, updateData_:bool):
        self.name = name_
        self.type = type_
        
        super().__init__(presetId_, symbolId_, updateData_)
    
    
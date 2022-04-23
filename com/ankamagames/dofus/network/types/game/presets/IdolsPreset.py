from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


class IdolsPreset(Preset):
    iconId:int
    idolIds:list[int]
    

    def init(self, iconId_:int, idolIds_:list[int], id_:int):
        self.iconId = iconId_
        self.idolIds = idolIds_
        
        super().__init__(id_)
    
    
from com.ankamagames.dofus.network.types.game.presets.PresetsContainerPreset import PresetsContainerPreset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class IconNamedPreset(PresetsContainerPreset):
    iconId:int
    name:str
    

    def init(self, iconId_:int, name_:str, presets_:list['Preset'], id_:int):
        self.iconId = iconId_
        self.name = name_
        
        super().__init__(presets_, id_)
    
    
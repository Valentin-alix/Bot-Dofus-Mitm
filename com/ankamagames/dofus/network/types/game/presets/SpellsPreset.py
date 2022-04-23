from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset
    


class SpellsPreset(Preset):
    spells:list['SpellForPreset']
    

    def init(self, spells_:list['SpellForPreset'], id_:int):
        self.spells = spells_
        
        super().__init__(id_)
    
    
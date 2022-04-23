from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
    


class FullStatsPreset(Preset):
    stats:list['CharacterCharacteristicForPreset']
    

    def init(self, stats_:list['CharacterCharacteristicForPreset'], id_:int):
        self.stats = stats_
        
        super().__init__(id_)
    
    
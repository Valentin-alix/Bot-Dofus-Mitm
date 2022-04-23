from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class PresetsMessage(NetworkMessage):
    presets:list['Preset']
    

    def init(self, presets_:list['Preset']):
        self.presets = presets_
        
        super().__init__()
    
    
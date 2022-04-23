from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
    


class ItemForPresetUpdateMessage(NetworkMessage):
    presetId:int
    presetItem:'ItemForPreset'
    

    def init(self, presetId_:int, presetItem_:'ItemForPreset'):
        self.presetId = presetId_
        self.presetItem = presetItem_
        
        super().__init__()
    
    
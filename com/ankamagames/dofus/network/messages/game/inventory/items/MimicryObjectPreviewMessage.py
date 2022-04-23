from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class MimicryObjectPreviewMessage(NetworkMessage):
    result:'ObjectItem'
    

    def init(self, result_:'ObjectItem'):
        self.result = result_
        
        super().__init__()
    
    
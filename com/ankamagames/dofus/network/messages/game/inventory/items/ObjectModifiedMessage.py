from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ObjectModifiedMessage(NetworkMessage):
    object:'ObjectItem'
    

    def init(self, object_:'ObjectItem'):
        self.object = object_
        
        super().__init__()
    
    
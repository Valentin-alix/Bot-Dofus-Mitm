from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ObjectAddedMessage(NetworkMessage):
    object:'ObjectItem'
    origin:int
    

    def init(self, object_:'ObjectItem', origin_:int):
        self.object = object_
        self.origin = origin_
        
        super().__init__()
    
    
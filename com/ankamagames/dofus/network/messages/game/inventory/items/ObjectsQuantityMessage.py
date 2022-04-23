from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity
    


class ObjectsQuantityMessage(NetworkMessage):
    objectsUIDAndQty:list['ObjectItemQuantity']
    

    def init(self, objectsUIDAndQty_:list['ObjectItemQuantity']):
        self.objectsUIDAndQty = objectsUIDAndQty_
        
        super().__init__()
    
    
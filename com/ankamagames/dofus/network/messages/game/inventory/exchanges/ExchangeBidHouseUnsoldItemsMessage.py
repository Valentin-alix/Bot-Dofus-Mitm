from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
    


class ExchangeBidHouseUnsoldItemsMessage(NetworkMessage):
    items:list['ObjectItemGenericQuantity']
    

    def init(self, items_:list['ObjectItemGenericQuantity']):
        self.items = items_
        
        super().__init__()
    
    
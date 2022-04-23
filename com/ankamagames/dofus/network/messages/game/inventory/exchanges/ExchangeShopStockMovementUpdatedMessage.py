from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
    


class ExchangeShopStockMovementUpdatedMessage(NetworkMessage):
    objectInfo:'ObjectItemToSell'
    

    def init(self, objectInfo_:'ObjectItemToSell'):
        self.objectInfo = objectInfo_
        
        super().__init__()
    
    
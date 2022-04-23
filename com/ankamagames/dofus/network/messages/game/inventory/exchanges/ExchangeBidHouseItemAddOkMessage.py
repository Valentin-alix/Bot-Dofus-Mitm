from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid
    


class ExchangeBidHouseItemAddOkMessage(NetworkMessage):
    itemInfo:'ObjectItemToSellInBid'
    

    def init(self, itemInfo_:'ObjectItemToSellInBid'):
        self.itemInfo = itemInfo_
        
        super().__init__()
    
    
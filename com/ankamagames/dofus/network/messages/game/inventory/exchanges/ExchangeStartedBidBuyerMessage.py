from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
    


class ExchangeStartedBidBuyerMessage(NetworkMessage):
    buyerDescriptor:'SellerBuyerDescriptor'
    

    def init(self, buyerDescriptor_:'SellerBuyerDescriptor'):
        self.buyerDescriptor = buyerDescriptor_
        
        super().__init__()
    
    
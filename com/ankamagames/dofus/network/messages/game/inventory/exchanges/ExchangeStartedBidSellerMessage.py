from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid
    


class ExchangeStartedBidSellerMessage(NetworkMessage):
    sellerDescriptor:'SellerBuyerDescriptor'
    objectsInfos:list['ObjectItemToSellInBid']
    

    def init(self, sellerDescriptor_:'SellerBuyerDescriptor', objectsInfos_:list['ObjectItemToSellInBid']):
        self.sellerDescriptor = sellerDescriptor_
        self.objectsInfos = objectsInfos_
        
        super().__init__()
    
    
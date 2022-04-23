from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop
    


class ExchangeStartOkHumanVendorMessage(NetworkMessage):
    sellerId:int
    objectsInfos:list['ObjectItemToSellInHumanVendorShop']
    

    def init(self, sellerId_:int, objectsInfos_:list['ObjectItemToSellInHumanVendorShop']):
        self.sellerId = sellerId_
        self.objectsInfos = objectsInfos_
        
        super().__init__()
    
    
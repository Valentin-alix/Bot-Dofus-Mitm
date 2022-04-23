from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
    


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    npcSellerId:int
    tokenId:int
    objectsInfos:list['ObjectItemToSellInNpcShop']
    

    def init(self, npcSellerId_:int, tokenId_:int, objectsInfos_:list['ObjectItemToSellInNpcShop']):
        self.npcSellerId = npcSellerId_
        self.tokenId = tokenId_
        self.objectsInfos = objectsInfos_
        
        super().__init__()
    
    
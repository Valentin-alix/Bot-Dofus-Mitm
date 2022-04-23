from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo
    


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    objectGID:int
    objectType:int
    itemTypeDescriptions:list['BidExchangerObjectInfo']
    

    def init(self, objectGID_:int, objectType_:int, itemTypeDescriptions_:list['BidExchangerObjectInfo']):
        self.objectGID = objectGID_
        self.objectType = objectType_
        self.itemTypeDescriptions = itemTypeDescriptions_
        
        super().__init__()
    
    
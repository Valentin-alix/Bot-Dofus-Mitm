from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
    


class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
    magicPoolStatus:int
    

    def init(self, magicPoolStatus_:int, objectInfo_:'ObjectItemNotInContainer', craftResult_:int):
        self.magicPoolStatus = magicPoolStatus_
        
        super().__init__(objectInfo_, craftResult_)
    
    
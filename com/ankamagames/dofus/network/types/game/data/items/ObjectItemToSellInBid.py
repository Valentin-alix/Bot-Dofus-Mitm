from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemToSellInBid(ObjectItemToSell):
    unsoldDelay:int
    

    def init(self, unsoldDelay_:int, objectGID_:int, effects_:list['ObjectEffect'], objectUID_:int, quantity_:int, objectPrice_:int):
        self.unsoldDelay = unsoldDelay_
        
        super().__init__(objectGID_, effects_, objectUID_, quantity_, objectPrice_)
    
    
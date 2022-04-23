from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectEffects import ObjectEffects
    


class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
    price:int
    effects:'ObjectEffects'
    date:int
    

    def init(self, price_:int, effects_:'ObjectEffects', date_:int, objectGID_:int, quantity_:int):
        self.price = price_
        self.effects = effects_
        self.date = date_
        
        super().__init__(objectGID_, quantity_)
    
    
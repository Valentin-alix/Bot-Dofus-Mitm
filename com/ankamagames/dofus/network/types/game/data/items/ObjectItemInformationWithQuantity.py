from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemInformationWithQuantity(ObjectItemMinimalInformation):
    quantity:int
    

    def init(self, quantity_:int, objectGID_:int, effects_:list['ObjectEffect']):
        self.quantity = quantity_
        
        super().__init__(objectGID_, effects_)
    
    
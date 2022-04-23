from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemToSell(Item):
    objectGID:int
    effects:list['ObjectEffect']
    objectUID:int
    quantity:int
    objectPrice:int
    

    def init(self, objectGID_:int, effects_:list['ObjectEffect'], objectUID_:int, quantity_:int, objectPrice_:int):
        self.objectGID = objectGID_
        self.effects = effects_
        self.objectUID = objectUID_
        self.quantity = quantity_
        self.objectPrice = objectPrice_
        
        super().__init__()
    
    
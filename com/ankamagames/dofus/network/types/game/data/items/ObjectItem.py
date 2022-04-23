from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItem(Item):
    position:int
    objectGID:int
    effects:list['ObjectEffect']
    objectUID:int
    quantity:int
    

    def init(self, position_:int, objectGID_:int, effects_:list['ObjectEffect'], objectUID_:int, quantity_:int):
        self.position = position_
        self.objectGID = objectGID_
        self.effects = effects_
        self.objectUID = objectUID_
        self.quantity = quantity_
        
        super().__init__()
    
    
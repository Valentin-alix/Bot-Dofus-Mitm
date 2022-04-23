from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemMinimalInformation(Item):
    objectGID:int
    effects:list['ObjectEffect']
    

    def init(self, objectGID_:int, effects_:list['ObjectEffect']):
        self.objectGID = objectGID_
        self.effects = effects_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
    objectPrice:int
    buyCriterion:str
    

    def init(self, objectPrice_:int, buyCriterion_:str, objectGID_:int, effects_:list['ObjectEffect']):
        self.objectPrice = objectPrice_
        self.buyCriterion = buyCriterion_
        
        super().__init__(objectGID_, effects_)
    
    
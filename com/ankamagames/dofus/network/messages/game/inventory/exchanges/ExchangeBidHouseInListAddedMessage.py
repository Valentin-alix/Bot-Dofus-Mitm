from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ExchangeBidHouseInListAddedMessage(NetworkMessage):
    itemUID:int
    objectGID:int
    objectType:int
    effects:list['ObjectEffect']
    prices:list[int]
    

    def init(self, itemUID_:int, objectGID_:int, objectType_:int, effects_:list['ObjectEffect'], prices_:list[int]):
        self.itemUID = itemUID_
        self.objectGID = objectGID_
        self.objectType = objectType_
        self.effects = effects_
        self.prices = prices_
        
        super().__init__()
    
    
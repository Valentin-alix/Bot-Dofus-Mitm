from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class BidExchangerObjectInfo(NetworkMessage):
    objectUID:int
    objectGID:int
    objectType:int
    effects:list['ObjectEffect']
    prices:list[int]
    

    def init(self, objectUID_:int, objectGID_:int, objectType_:int, effects_:list['ObjectEffect'], prices_:list[int]):
        self.objectUID = objectUID_
        self.objectGID = objectGID_
        self.objectType = objectType_
        self.effects = effects_
        self.prices = prices_
        
        super().__init__()
    
    
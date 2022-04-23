from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem
    


class EvolutiveObjectRecycleResultMessage(NetworkMessage):
    recycledItems:list['RecycledItem']
    

    def init(self, recycledItems_:list['RecycledItem']):
        self.recycledItems = recycledItems_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.GoldItem import GoldItem
    


class GoldAddedMessage(NetworkMessage):
    gold:'GoldItem'
    

    def init(self, gold_:'GoldItem'):
        self.gold = gold_
        
        super().__init__()
    
    
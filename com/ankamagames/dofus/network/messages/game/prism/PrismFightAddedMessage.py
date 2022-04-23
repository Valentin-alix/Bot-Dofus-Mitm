from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation
    


class PrismFightAddedMessage(NetworkMessage):
    fight:'PrismFightersInformation'
    

    def init(self, fight_:'PrismFightersInformation'):
        self.fight = fight_
        
        super().__init__()
    
    
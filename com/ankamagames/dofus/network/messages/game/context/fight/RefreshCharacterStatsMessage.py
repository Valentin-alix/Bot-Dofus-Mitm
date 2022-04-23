from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    


class RefreshCharacterStatsMessage(NetworkMessage):
    fighterId:int
    stats:'GameFightCharacteristics'
    

    def init(self, fighterId_:int, stats_:'GameFightCharacteristics'):
        self.fighterId = fighterId_
        self.stats = stats_
        
        super().__init__()
    
    
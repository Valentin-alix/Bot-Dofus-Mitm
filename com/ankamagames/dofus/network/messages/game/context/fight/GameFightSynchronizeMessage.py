from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
    


class GameFightSynchronizeMessage(NetworkMessage):
    fighters:list['GameFightFighterInformations']
    

    def init(self, fighters_:list['GameFightFighterInformations']):
        self.fighters = fighters_
        
        super().__init__()
    
    
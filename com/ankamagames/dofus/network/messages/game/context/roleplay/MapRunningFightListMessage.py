from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations
    


class MapRunningFightListMessage(NetworkMessage):
    fights:list['FightExternalInformations']
    

    def init(self, fights_:list['FightExternalInformations']):
        self.fights = fights_
        
        super().__init__()
    
    
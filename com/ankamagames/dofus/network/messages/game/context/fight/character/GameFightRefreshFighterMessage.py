from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
    


class GameFightRefreshFighterMessage(NetworkMessage):
    informations:'GameContextActorInformations'
    

    def init(self, informations_:'GameContextActorInformations'):
        self.informations = informations_
        
        super().__init__()
    
    
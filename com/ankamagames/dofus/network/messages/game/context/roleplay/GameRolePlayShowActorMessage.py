from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    


class GameRolePlayShowActorMessage(NetworkMessage):
    informations:'GameRolePlayActorInformations'
    

    def init(self, informations_:'GameRolePlayActorInformations'):
        self.informations = informations_
        
        super().__init__()
    
    
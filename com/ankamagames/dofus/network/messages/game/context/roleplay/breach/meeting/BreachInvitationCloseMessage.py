from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachInvitationCloseMessage(NetworkMessage):
    host:'CharacterMinimalInformations'
    

    def init(self, host_:'CharacterMinimalInformations'):
        self.host = host_
        
        super().__init__()
    
    
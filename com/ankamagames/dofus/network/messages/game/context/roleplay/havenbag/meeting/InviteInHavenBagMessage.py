from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class InviteInHavenBagMessage(NetworkMessage):
    guestInformations:'CharacterMinimalInformations'
    accept:bool
    

    def init(self, guestInformations_:'CharacterMinimalInformations', accept_:bool):
        self.guestInformations = guestInformations_
        self.accept = accept_
        
        super().__init__()
    
    
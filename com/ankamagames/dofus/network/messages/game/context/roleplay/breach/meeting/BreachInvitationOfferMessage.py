from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class BreachInvitationOfferMessage(NetworkMessage):
    host:'CharacterMinimalInformations'
    timeLeftBeforeCancel:int
    

    def init(self, host_:'CharacterMinimalInformations', timeLeftBeforeCancel_:int):
        self.host = host_
        self.timeLeftBeforeCancel = timeLeftBeforeCancel_
        
        super().__init__()
    
    
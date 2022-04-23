from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    


class InviteInHavenBagOfferMessage(NetworkMessage):
    hostInformations:'CharacterMinimalInformations'
    timeLeftBeforeCancel:int
    

    def init(self, hostInformations_:'CharacterMinimalInformations', timeLeftBeforeCancel_:int):
        self.hostInformations = hostInformations_
        self.timeLeftBeforeCancel = timeLeftBeforeCancel_
        
        super().__init__()
    
    
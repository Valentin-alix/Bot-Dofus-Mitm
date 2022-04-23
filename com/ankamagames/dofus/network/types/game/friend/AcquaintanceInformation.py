from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AcquaintanceInformation(AbstractContactInformations):
    playerState:int
    

    def init(self, playerState_:int, accountId_:int, accountTag_:'AccountTagInformation'):
        self.playerState = playerState_
        
        super().__init__(accountId_, accountTag_)
    
    
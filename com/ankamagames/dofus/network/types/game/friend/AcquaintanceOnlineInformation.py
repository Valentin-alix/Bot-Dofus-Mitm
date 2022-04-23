from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AcquaintanceOnlineInformation(AcquaintanceInformation):
    playerId:int
    playerName:str
    moodSmileyId:int
    status:'PlayerStatus'
    

    def init(self, playerId_:int, playerName_:str, moodSmileyId_:int, status_:'PlayerStatus', playerState_:int, accountId_:int, accountTag_:'AccountTagInformation'):
        self.playerId = playerId_
        self.playerName = playerName_
        self.moodSmileyId = moodSmileyId_
        self.status = status_
        
        super().__init__(playerState_, accountId_, accountTag_)
    
    
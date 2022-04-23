from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendInformations(AbstractContactInformations):
    playerState:int
    lastConnection:int
    achievementPoints:int
    leagueId:int
    ladderPosition:int
    

    def init(self, playerState_:int, lastConnection_:int, achievementPoints_:int, leagueId_:int, ladderPosition_:int, accountId_:int, accountTag_:'AccountTagInformation'):
        self.playerState = playerState_
        self.lastConnection = lastConnection_
        self.achievementPoints = achievementPoints_
        self.leagueId = leagueId_
        self.ladderPosition = ladderPosition_
        
        super().__init__(accountId_, accountTag_)
    
    
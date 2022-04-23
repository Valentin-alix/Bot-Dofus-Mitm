from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendOnlineInformations(FriendInformations):
    playerId:int
    playerName:str
    level:int
    alignmentSide:int
    breed:int
    guildInfo:'GuildInformations'
    moodSmileyId:int
    status:'PlayerStatus'
    sex:bool
    havenBagShared:bool
    sex:bool
    havenBagShared:bool
    

    def init(self, playerId_:int, playerName_:str, level_:int, alignmentSide_:int, breed_:int, guildInfo_:'GuildInformations', moodSmileyId_:int, status_:'PlayerStatus', sex_:bool, havenBagShared_:bool, playerState_:int, lastConnection_:int, achievementPoints_:int, leagueId_:int, ladderPosition_:int, accountId_:int, accountTag_:'AccountTagInformation'):
        self.playerId = playerId_
        self.playerName = playerName_
        self.level = level_
        self.alignmentSide = alignmentSide_
        self.breed = breed_
        self.guildInfo = guildInfo_
        self.moodSmileyId = moodSmileyId_
        self.status = status_
        self.sex = sex_
        self.havenBagShared = havenBagShared_
        
        super().__init__(playerState_, lastConnection_, achievementPoints_, leagueId_, ladderPosition_, accountId_, accountTag_)
    
    
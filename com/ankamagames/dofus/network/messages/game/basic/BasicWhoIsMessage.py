from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos
    


class BasicWhoIsMessage(NetworkMessage):
    position:int
    accountTag:'AccountTagInformation'
    accountId:int
    playerName:str
    playerId:int
    areaId:int
    serverId:int
    originServerId:int
    socialGroups:list['AbstractSocialGroupInfos']
    playerState:int
    self:bool
    verbose:bool
    self:bool
    verbose:bool
    

    def init(self, position_:int, accountTag_:'AccountTagInformation', accountId_:int, playerName_:str, playerId_:int, areaId_:int, serverId_:int, originServerId_:int, socialGroups_:list['AbstractSocialGroupInfos'], playerState_:int, self_:bool, verbose_:bool):
        self.position = position_
        self.accountTag = accountTag_
        self.accountId = accountId_
        self.playerName = playerName_
        self.playerId = playerId_
        self.areaId = areaId_
        self.serverId = serverId_
        self.originServerId = originServerId_
        self.socialGroups = socialGroups_
        self.playerState = playerState_
        self.self = self_
        self.verbose = verbose_
        
        super().__init__()
    
    
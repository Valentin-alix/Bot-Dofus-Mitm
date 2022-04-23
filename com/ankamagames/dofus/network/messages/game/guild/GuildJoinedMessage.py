from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildJoinedMessage(NetworkMessage):
    guildInfo:'GuildInformations'
    rankId:int
    

    def init(self, guildInfo_:'GuildInformations', rankId_:int):
        self.guildInfo = guildInfo_
        self.rankId = rankId_
        
        super().__init__()
    
    
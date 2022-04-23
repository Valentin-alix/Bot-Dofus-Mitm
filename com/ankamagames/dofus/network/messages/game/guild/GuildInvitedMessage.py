from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class GuildInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    guildInfo:'BasicGuildInformations'
    

    def init(self, recruterId_:int, recruterName_:str, guildInfo_:'BasicGuildInformations'):
        self.recruterId = recruterId_
        self.recruterName = recruterName_
        self.guildInfo = guildInfo_
        
        super().__init__()
    
    
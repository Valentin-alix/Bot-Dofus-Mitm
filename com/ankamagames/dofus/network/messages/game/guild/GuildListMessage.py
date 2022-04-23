from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildListMessage(NetworkMessage):
    guilds:list['GuildInformations']
    

    def init(self, guilds_:list['GuildInformations']):
        self.guilds = guilds_
        
        super().__init__()
    
    
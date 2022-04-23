from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember
    


class GuildInformationsMembersMessage(NetworkMessage):
    members:list['GuildMember']
    

    def init(self, members_:list['GuildMember']):
        self.members = members_
        
        super().__init__()
    
    
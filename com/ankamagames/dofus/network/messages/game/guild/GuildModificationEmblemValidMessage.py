from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildModificationEmblemValidMessage(NetworkMessage):
    guildEmblem:'GuildEmblem'
    

    def init(self, guildEmblem_:'GuildEmblem'):
        self.guildEmblem = guildEmblem_
        
        super().__init__()
    
    
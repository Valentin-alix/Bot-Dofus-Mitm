from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildCreationValidMessage(NetworkMessage):
    guildName:str
    guildEmblem:'GuildEmblem'
    

    def init(self, guildName_:str, guildEmblem_:'GuildEmblem'):
        self.guildName = guildName_
        self.guildEmblem = guildEmblem_
        
        super().__init__()
    
    
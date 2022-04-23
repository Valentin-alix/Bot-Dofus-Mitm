from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildRankInformation import GuildRankInformation
    


class UpdateAllGuildRankRequestMessage(NetworkMessage):
    ranks:list['GuildRankInformation']
    

    def init(self, ranks_:list['GuildRankInformation']):
        self.ranks = ranks_
        
        super().__init__()
    
    
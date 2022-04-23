from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildRankInformation import GuildRankInformation
    


class UpdateGuildRankRequestMessage(NetworkMessage):
    rank:'GuildRankInformation'
    

    def init(self, rank_:'GuildRankInformation'):
        self.rank = rank_
        
        super().__init__()
    
    
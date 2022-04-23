from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildRankMinimalInformation import GuildRankMinimalInformation
    


class GuildRankActivity(GuildLogbookEntryBasicInformation):
    rankActivityType:int
    guildRankMinimalInfos:'GuildRankMinimalInformation'
    

    def init(self, rankActivityType_:int, guildRankMinimalInfos_:'GuildRankMinimalInformation', id_:int, date_:int):
        self.rankActivityType = rankActivityType_
        self.guildRankMinimalInfos = guildRankMinimalInfos_
        
        super().__init__(id_, date_)
    
    
from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildRankMinimalInformation import GuildRankMinimalInformation
    


class GuildPlayerRankUpdateActivity(GuildLogbookEntryBasicInformation):
    guildRankMinimalInfos:'GuildRankMinimalInformation'
    playerId:int
    playerName:str
    

    def init(self, guildRankMinimalInfos_:'GuildRankMinimalInformation', playerId_:int, playerName_:str, id_:int, date_:int):
        self.guildRankMinimalInfos = guildRankMinimalInfos_
        self.playerId = playerId_
        self.playerName = playerName_
        
        super().__init__(id_, date_)
    
    
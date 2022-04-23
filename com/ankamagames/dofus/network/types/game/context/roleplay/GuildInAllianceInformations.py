from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildInAllianceInformations(GuildInformations):
    nbMembers:int
    joinDate:int
    

    def init(self, nbMembers_:int, joinDate_:int, guildEmblem_:'GuildEmblem', guildId_:int, guildName_:str, guildLevel_:int):
        self.nbMembers = nbMembers_
        self.joinDate = joinDate_
        
        super().__init__(guildEmblem_, guildId_, guildName_, guildLevel_)
    
    
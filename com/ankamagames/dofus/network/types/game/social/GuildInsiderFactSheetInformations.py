from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
    leaderName:str
    nbConnectedMembers:int
    nbTaxCollectors:int
    

    def init(self, leaderName_:str, nbConnectedMembers_:int, nbTaxCollectors_:int, leaderId_:int, nbMembers_:int, lastActivityDay_:int, recruitment_:'GuildRecruitmentInformation', nbPendingApply_:int, guildEmblem_:'GuildEmblem', guildId_:int, guildName_:str, guildLevel_:int):
        self.leaderName = leaderName_
        self.nbConnectedMembers = nbConnectedMembers_
        self.nbTaxCollectors = nbTaxCollectors_
        
        super().__init__(leaderId_, nbMembers_, lastActivityDay_, recruitment_, nbPendingApply_, guildEmblem_, guildId_, guildName_, guildLevel_)
    
    
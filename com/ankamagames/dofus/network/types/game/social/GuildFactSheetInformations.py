from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildFactSheetInformations(GuildInformations):
    leaderId:int
    nbMembers:int
    lastActivityDay:int
    recruitment:'GuildRecruitmentInformation'
    nbPendingApply:int
    

    def init(self, leaderId_:int, nbMembers_:int, lastActivityDay_:int, recruitment_:'GuildRecruitmentInformation', nbPendingApply_:int, guildEmblem_:'GuildEmblem', guildId_:int, guildName_:str, guildLevel_:int):
        self.leaderId = leaderId_
        self.nbMembers = nbMembers_
        self.lastActivityDay = lastActivityDay_
        self.recruitment = recruitment_
        self.nbPendingApply = nbPendingApply_
        
        super().__init__(guildEmblem_, guildId_, guildName_, guildLevel_)
    
    
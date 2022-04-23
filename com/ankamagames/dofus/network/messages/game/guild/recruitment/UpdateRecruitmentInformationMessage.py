from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
    


class UpdateRecruitmentInformationMessage(NetworkMessage):
    recruitmentData:'GuildRecruitmentInformation'
    

    def init(self, recruitmentData_:'GuildRecruitmentInformation'):
        self.recruitmentData = recruitmentData_
        
        super().__init__()
    
    
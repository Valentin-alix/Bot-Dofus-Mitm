from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience
    


class JobExperienceUpdateMessage(NetworkMessage):
    experiencesUpdate:'JobExperience'
    

    def init(self, experiencesUpdate_:'JobExperience'):
        self.experiencesUpdate = experiencesUpdate_
        
        super().__init__()
    
    
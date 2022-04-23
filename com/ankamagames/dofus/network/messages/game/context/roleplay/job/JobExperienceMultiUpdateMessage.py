from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience
    


class JobExperienceMultiUpdateMessage(NetworkMessage):
    experiencesUpdate:list['JobExperience']
    

    def init(self, experiencesUpdate_:list['JobExperience']):
        self.experiencesUpdate = experiencesUpdate_
        
        super().__init__()
    
    
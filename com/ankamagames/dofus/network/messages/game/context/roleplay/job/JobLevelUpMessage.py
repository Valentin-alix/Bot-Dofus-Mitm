from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription
    


class JobLevelUpMessage(NetworkMessage):
    newLevel:int
    jobsDescription:'JobDescription'
    

    def init(self, newLevel_:int, jobsDescription_:'JobDescription'):
        self.newLevel = newLevel_
        self.jobsDescription = jobsDescription_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
    


class JobCrafterDirectoryListEntry(NetworkMessage):
    playerInfo:'JobCrafterDirectoryEntryPlayerInfo'
    jobInfo:'JobCrafterDirectoryEntryJobInfo'
    

    def init(self, playerInfo_:'JobCrafterDirectoryEntryPlayerInfo', jobInfo_:'JobCrafterDirectoryEntryJobInfo'):
        self.playerInfo = playerInfo_
        self.jobInfo = jobInfo_
        
        super().__init__()
    
    
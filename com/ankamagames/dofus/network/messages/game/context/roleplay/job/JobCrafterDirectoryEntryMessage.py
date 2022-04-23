from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class JobCrafterDirectoryEntryMessage(NetworkMessage):
    playerInfo:'JobCrafterDirectoryEntryPlayerInfo'
    jobInfoList:list['JobCrafterDirectoryEntryJobInfo']
    playerLook:'EntityLook'
    

    def init(self, playerInfo_:'JobCrafterDirectoryEntryPlayerInfo', jobInfoList_:list['JobCrafterDirectoryEntryJobInfo'], playerLook_:'EntityLook'):
        self.playerInfo = playerInfo_
        self.jobInfoList = jobInfoList_
        self.playerLook = playerLook_
        
        super().__init__()
    
    
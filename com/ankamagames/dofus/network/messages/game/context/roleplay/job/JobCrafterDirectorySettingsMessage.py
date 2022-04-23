from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings
    


class JobCrafterDirectorySettingsMessage(NetworkMessage):
    craftersSettings:list['JobCrafterDirectorySettings']
    

    def init(self, craftersSettings_:list['JobCrafterDirectorySettings']):
        self.craftersSettings = craftersSettings_
        
        super().__init__()
    
    
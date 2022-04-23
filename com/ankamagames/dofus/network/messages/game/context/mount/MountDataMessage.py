from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class MountDataMessage(NetworkMessage):
    mountData:'MountClientData'
    

    def init(self, mountData_:'MountClientData'):
        self.mountData = mountData_
        
        super().__init__()
    
    
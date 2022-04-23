from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class ExchangeMountsStableAddMessage(NetworkMessage):
    mountDescription:list['MountClientData']
    

    def init(self, mountDescription_:list['MountClientData']):
        self.mountDescription = mountDescription_
        
        super().__init__()
    
    
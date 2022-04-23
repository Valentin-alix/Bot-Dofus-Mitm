from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class ExchangeStartOkMountWithOutPaddockMessage(NetworkMessage):
    stabledMountsDescription:list['MountClientData']
    

    def init(self, stabledMountsDescription_:list['MountClientData']):
        self.stabledMountsDescription = stabledMountsDescription_
        
        super().__init__()
    
    
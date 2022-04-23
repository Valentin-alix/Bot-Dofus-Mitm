from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class BasicWhoIsRequestMessage(NetworkMessage):
    verbose:bool
    target:'AbstractPlayerSearchInformation'
    

    def init(self, verbose_:bool, target_:'AbstractPlayerSearchInformation'):
        self.verbose = verbose_
        self.target = target_
        
        super().__init__()
    
    
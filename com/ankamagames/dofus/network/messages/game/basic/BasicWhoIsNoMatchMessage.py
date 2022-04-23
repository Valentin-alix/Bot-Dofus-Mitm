from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class BasicWhoIsNoMatchMessage(NetworkMessage):
    target:'AbstractPlayerSearchInformation'
    

    def init(self, target_:'AbstractPlayerSearchInformation'):
        self.target = target_
        
        super().__init__()
    
    
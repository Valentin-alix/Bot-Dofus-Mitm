from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class IgnoredAddRequestMessage(NetworkMessage):
    target:'AbstractPlayerSearchInformation'
    session:bool
    

    def init(self, target_:'AbstractPlayerSearchInformation', session_:bool):
        self.target = target_
        self.session = session_
        
        super().__init__()
    
    
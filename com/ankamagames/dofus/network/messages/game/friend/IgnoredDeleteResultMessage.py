from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IgnoredDeleteResultMessage(NetworkMessage):
    tag:'AccountTagInformation'
    success:bool
    session:bool
    success:bool
    session:bool
    

    def init(self, tag_:'AccountTagInformation', success_:bool, session_:bool):
        self.tag = tag_
        self.success = success_
        self.session = session_
        
        super().__init__()
    
    
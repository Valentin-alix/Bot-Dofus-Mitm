from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendDeleteResultMessage(NetworkMessage):
    success:bool
    tag:'AccountTagInformation'
    

    def init(self, success_:bool, tag_:'AccountTagInformation'):
        self.success = success_
        self.tag = tag_
        
        super().__init__()
    
    
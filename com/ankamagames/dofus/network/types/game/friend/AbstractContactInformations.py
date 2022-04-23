from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class AbstractContactInformations(NetworkMessage):
    accountId:int
    accountTag:'AccountTagInformation'
    

    def init(self, accountId_:int, accountTag_:'AccountTagInformation'):
        self.accountId = accountId_
        self.accountTag = accountTag_
        
        super().__init__()
    
    
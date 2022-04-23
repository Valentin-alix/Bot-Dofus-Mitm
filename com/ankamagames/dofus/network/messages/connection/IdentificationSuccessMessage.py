from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IdentificationSuccessMessage(NetworkMessage):
    login:str
    accountTag:'AccountTagInformation'
    accountId:int
    communityId:int
    secretQuestion:str
    accountCreation:int
    subscriptionElapsedDuration:int
    subscriptionEndDate:int
    havenbagAvailableRoom:int
    hasRights:bool
    hasConsoleRight:bool
    wasAlreadyConnected:bool
    isAccountForced:bool
    hasRights:bool
    hasConsoleRight:bool
    wasAlreadyConnected:bool
    isAccountForced:bool
    

    def init(self, login_:str, accountTag_:'AccountTagInformation', accountId_:int, communityId_:int, secretQuestion_:str, accountCreation_:int, subscriptionElapsedDuration_:int, subscriptionEndDate_:int, havenbagAvailableRoom_:int, hasRights_:bool, hasConsoleRight_:bool, wasAlreadyConnected_:bool, isAccountForced_:bool):
        self.login = login_
        self.accountTag = accountTag_
        self.accountId = accountId_
        self.communityId = communityId_
        self.secretQuestion = secretQuestion_
        self.accountCreation = accountCreation_
        self.subscriptionElapsedDuration = subscriptionElapsedDuration_
        self.subscriptionEndDate = subscriptionEndDate_
        self.havenbagAvailableRoom = havenbagAvailableRoom_
        self.hasRights = hasRights_
        self.hasConsoleRight = hasConsoleRight_
        self.wasAlreadyConnected = wasAlreadyConnected_
        self.isAccountForced = isAccountForced_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    loginToken:str
    

    def init(self, loginToken_:str, login_:str, accountTag_:'AccountTagInformation', accountId_:int, communityId_:int, secretQuestion_:str, accountCreation_:int, subscriptionElapsedDuration_:int, subscriptionEndDate_:int, havenbagAvailableRoom_:int, hasRights_:bool, hasConsoleRight_:bool, wasAlreadyConnected_:bool, isAccountForced_:bool):
        self.loginToken = loginToken_
        
        super().__init__(login_, accountTag_, accountId_, communityId_, secretQuestion_, accountCreation_, subscriptionElapsedDuration_, subscriptionEndDate_, havenbagAvailableRoom_, hasRights_, hasConsoleRight_, wasAlreadyConnected_, isAccountForced_)
    
    
from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.version.Version import Version
    


class IdentificationAccountForceMessage(IdentificationMessage):
    forcerAccountLogin:str
    

    def init(self, forcerAccountLogin_:str, version_:'Version', lang_:str, credentials_:list[int], serverId_:int, sessionOptionalSalt_:int, failedAttempts_:list[int], autoconnect_:bool, useCertificate_:bool, useLoginToken_:bool):
        self.forcerAccountLogin = forcerAccountLogin_
        
        super().__init__(version_, lang_, credentials_, serverId_, sessionOptionalSalt_, failedAttempts_, autoconnect_, useCertificate_, useLoginToken_)
    
    
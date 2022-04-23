from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.version.Version import Version
    


class IdentificationMessage(NetworkMessage):
    version:'Version'
    lang:str
    credentials:list[int]
    serverId:int
    sessionOptionalSalt:int
    failedAttempts:list[int]
    autoconnect:bool
    useCertificate:bool
    useLoginToken:bool
    autoconnect:bool
    useCertificate:bool
    useLoginToken:bool
    

    def init(self, version_:'Version', lang_:str, credentials_:list[int], serverId_:int, sessionOptionalSalt_:int, failedAttempts_:list[int], autoconnect_:bool, useCertificate_:bool, useLoginToken_:bool):
        self.version = version_
        self.lang = lang_
        self.credentials = credentials_
        self.serverId = serverId_
        self.sessionOptionalSalt = sessionOptionalSalt_
        self.failedAttempts = failedAttempts_
        self.autoconnect = autoconnect_
        self.useCertificate = useCertificate_
        self.useLoginToken = useLoginToken_
        
        super().__init__()
    
    
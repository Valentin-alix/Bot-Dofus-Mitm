from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.version.Version import Version
    


class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
    requiredVersion:'Version'
    

    def init(self, requiredVersion_:'Version', reason_:int):
        self.requiredVersion = requiredVersion_
        
        super().__init__(reason_)
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class TaxCollectorStaticInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    guildIdentity:'GuildInformations'
    callerId:int
    

    def init(self, firstNameId_:int, lastNameId_:int, guildIdentity_:'GuildInformations', callerId_:int):
        self.firstNameId = firstNameId_
        self.lastNameId = lastNameId_
        self.guildIdentity = guildIdentity_
        self.callerId = callerId_
        
        super().__init__()
    
    
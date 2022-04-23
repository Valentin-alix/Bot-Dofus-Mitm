from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
    allianceIdentity:'AllianceInformations'
    

    def init(self, allianceIdentity_:'AllianceInformations', firstNameId_:int, lastNameId_:int, guildIdentity_:'GuildInformations', callerId_:int):
        self.allianceIdentity = allianceIdentity_
        
        super().__init__(firstNameId_, lastNameId_, guildIdentity_, callerId_)
    
    
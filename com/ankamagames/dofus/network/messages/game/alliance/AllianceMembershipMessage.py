from com.ankamagames.dofus.network.messages.game.alliance.AllianceJoinedMessage import AllianceJoinedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AllianceMembershipMessage(AllianceJoinedMessage):
    

    def init(self, allianceInfo_:'AllianceInformations', enabled_:bool, leadingGuildId_:int):
        
        super().__init__(allianceInfo_, enabled_, leadingGuildId_)
    
    
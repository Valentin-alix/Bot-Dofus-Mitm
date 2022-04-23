from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationRequestMessage import PartyInvitationRequestMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class PartyInvitationArenaRequestMessage(PartyInvitationRequestMessage):
    

    def init(self, target_:'AbstractPlayerSearchInformation'):
        
        super().__init__(target_)
    
    
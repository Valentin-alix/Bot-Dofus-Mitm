from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
    


class PartyNewGuestMessage(AbstractPartyEventMessage):
    guest:'PartyGuestInformations'
    

    def init(self, guest_:'PartyGuestInformations', partyId_:int):
        self.guest = guest_
        
        super().__init__(partyId_)
    
    
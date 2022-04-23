from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationCancelledForGuestMessage(AbstractPartyMessage):
    cancelerId:int
    

    def init(self, cancelerId_:int, partyId_:int):
        self.cancelerId = cancelerId_
        
        super().__init__(partyId_)
    
    
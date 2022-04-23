from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyRefuseInvitationNotificationMessage(AbstractPartyEventMessage):
    guestId:int
    

    def init(self, guestId_:int, partyId_:int):
        self.guestId = guestId_
        
        super().__init__(partyId_)
    
    
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    cancelerId:int
    guestId:int
    

    def init(self, cancelerId_:int, guestId_:int, partyId_:int):
        self.cancelerId = cancelerId_
        self.guestId = guestId_
        
        super().__init__(partyId_)
    
    
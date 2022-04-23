from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyCannotJoinErrorMessage(AbstractPartyMessage):
    reason:int
    

    def init(self, reason_:int, partyId_:int):
        self.reason = reason_
        
        super().__init__(partyId_)
    
    
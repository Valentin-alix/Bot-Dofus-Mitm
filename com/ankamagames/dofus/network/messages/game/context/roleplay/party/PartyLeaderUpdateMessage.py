from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyLeaderUpdateMessage(AbstractPartyEventMessage):
    partyLeaderId:int
    

    def init(self, partyLeaderId_:int, partyId_:int):
        self.partyLeaderId = partyLeaderId_
        
        super().__init__(partyId_)
    
    
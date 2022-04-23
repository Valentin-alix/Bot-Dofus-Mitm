from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationMessage(AbstractPartyMessage):
    partyType:int
    partyName:str
    maxParticipants:int
    fromId:int
    fromName:str
    toId:int
    

    def init(self, partyType_:int, partyName_:str, maxParticipants_:int, fromId_:int, fromName_:str, toId_:int, partyId_:int):
        self.partyType = partyType_
        self.partyName = partyName_
        self.maxParticipants = maxParticipants_
        self.fromId = fromId_
        self.fromName = fromName_
        self.toId = toId_
        
        super().__init__(partyId_)
    
    
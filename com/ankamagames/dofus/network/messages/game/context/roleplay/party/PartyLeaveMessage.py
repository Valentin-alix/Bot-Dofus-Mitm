from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyLeaveMessage(AbstractPartyMessage):
    

    def init(self, partyId_:int):
        
        super().__init__(partyId_)
    
    
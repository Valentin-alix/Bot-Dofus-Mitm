from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyLoyaltyStatusMessage(AbstractPartyMessage):
    loyal:bool
    

    def init(self, loyal_:bool, partyId_:int):
        self.loyal = loyal_
        
        super().__init__(partyId_)
    
    
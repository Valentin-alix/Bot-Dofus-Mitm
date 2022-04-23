from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyRestrictedMessage(AbstractPartyMessage):
    restricted:bool
    

    def init(self, restricted_:bool, partyId_:int):
        self.restricted = restricted_
        
        super().__init__(partyId_)
    
    
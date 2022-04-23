from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickedByMessage(AbstractPartyMessage):
    kickerId:int
    

    def init(self, kickerId_:int, partyId_:int):
        self.kickerId = kickerId_
        
        super().__init__(partyId_)
    
    
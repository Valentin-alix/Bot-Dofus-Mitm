from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickRequestMessage(AbstractPartyMessage):
    playerId:int
    

    def init(self, playerId_:int, partyId_:int):
        self.playerId = playerId_
        
        super().__init__(partyId_)
    
    
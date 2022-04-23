from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import PartyMemberRemoveMessage


class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
    kickerId:int
    

    def init(self, kickerId_:int, leavingPlayerId_:int, partyId_:int):
        self.kickerId = kickerId_
        
        super().__init__(leavingPlayerId_, partyId_)
    
    
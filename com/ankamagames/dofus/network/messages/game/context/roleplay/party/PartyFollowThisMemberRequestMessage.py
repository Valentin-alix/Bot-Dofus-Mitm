from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage


class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
    enabled:bool
    

    def init(self, enabled_:bool, playerId_:int, partyId_:int):
        self.enabled = enabled_
        
        super().__init__(playerId_, partyId_)
    
    
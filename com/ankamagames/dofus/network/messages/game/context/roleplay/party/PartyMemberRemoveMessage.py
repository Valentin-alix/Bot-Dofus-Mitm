from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyMemberRemoveMessage(AbstractPartyEventMessage):
    leavingPlayerId:int
    

    def init(self, leavingPlayerId_:int, partyId_:int):
        self.leavingPlayerId = leavingPlayerId_
        
        super().__init__(partyId_)
    
    
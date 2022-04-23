from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    floor:int
    room:int
    

    def init(self, floor_:int, room_:int, reason_:int, memberId_:int, memberAccountId_:int, memberName_:str, fightId_:int, timeBeforeFightStart_:int, partyId_:int):
        self.floor = floor_
        self.room = room_
        
        super().__init__(reason_, memberId_, memberAccountId_, memberName_, fightId_, timeBeforeFightStart_, partyId_)
    
    
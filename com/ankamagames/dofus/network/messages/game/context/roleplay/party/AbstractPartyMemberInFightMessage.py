from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    reason:int
    memberId:int
    memberAccountId:int
    memberName:str
    fightId:int
    timeBeforeFightStart:int
    

    def init(self, reason_:int, memberId_:int, memberAccountId_:int, memberName_:str, fightId_:int, timeBeforeFightStart_:int, partyId_:int):
        self.reason = reason_
        self.memberId = memberId_
        self.memberAccountId = memberAccountId_
        self.memberName = memberName_
        self.fightId = fightId_
        self.timeBeforeFightStart = timeBeforeFightStart_
        
        super().__init__(partyId_)
    
    
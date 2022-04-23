from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    followedId:int
    success:bool
    isFollowed:bool
    success:bool
    isFollowed:bool
    

    def init(self, followedId_:int, success_:bool, isFollowed_:bool, partyId_:int):
        self.followedId = followedId_
        self.success = success_
        self.isFollowed = isFollowed_
        
        super().__init__(partyId_)
    
    
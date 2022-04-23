from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    memberId:int
    rankId:int
    experienceGivenPercent:int
    

    def init(self, memberId_:int, rankId_:int, experienceGivenPercent_:int):
        self.memberId = memberId_
        self.rankId = rankId_
        self.experienceGivenPercent = experienceGivenPercent_
        
        super().__init__()
    
    
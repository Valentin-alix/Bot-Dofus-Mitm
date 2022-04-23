from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetsListRequestMessage(NetworkMessage):
    challengeId:int
    

    def init(self, challengeId_:int):
        self.challengeId = challengeId_
        
        super().__init__()
    
    
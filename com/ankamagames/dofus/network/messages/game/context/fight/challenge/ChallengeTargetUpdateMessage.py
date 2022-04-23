from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    challengeId:int
    targetId:int
    

    def init(self, challengeId_:int, targetId_:int):
        self.challengeId = challengeId_
        self.targetId = targetId_
        
        super().__init__()
    
    
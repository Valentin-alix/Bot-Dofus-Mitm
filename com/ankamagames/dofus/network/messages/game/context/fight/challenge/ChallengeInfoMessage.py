from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    

    def init(self, challengeId_:int, targetId_:int, xpBonus_:int, dropBonus_:int):
        self.challengeId = challengeId_
        self.targetId = targetId_
        self.xpBonus = xpBonus_
        self.dropBonus = dropBonus_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeResultMessage(NetworkMessage):
    challengeId:int
    success:bool
    

    def init(self, challengeId_:int, success_:bool):
        self.challengeId = challengeId_
        self.success = success_
        
        super().__init__()
    
    
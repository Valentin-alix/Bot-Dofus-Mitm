from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementRewardErrorMessage(NetworkMessage):
    achievementId:int
    

    def init(self, achievementId_:int):
        self.achievementId = achievementId_
        
        super().__init__()
    
    
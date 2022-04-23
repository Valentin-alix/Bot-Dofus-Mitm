from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


class AchievementAchievedRewardable(AchievementAchieved):
    finishedlevel:int
    

    def init(self, finishedlevel_:int, id_:int, achievedBy_:int):
        self.finishedlevel = finishedlevel_
        
        super().__init__(id_, achievedBy_)
    
    
from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective


class AchievementStartedObjective(AchievementObjective):
    value:int
    

    def init(self, value_:int, id_:int, maxValue_:int):
        self.value = value_
        
        super().__init__(id_, maxValue_)
    
    
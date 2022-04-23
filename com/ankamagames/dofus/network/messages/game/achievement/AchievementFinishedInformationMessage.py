from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import AchievementFinishedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable
    


class AchievementFinishedInformationMessage(AchievementFinishedMessage):
    name:str
    playerId:int
    

    def init(self, name_:str, playerId_:int, achievement_:'AchievementAchievedRewardable'):
        self.name = name_
        self.playerId = playerId_
        
        super().__init__(achievement_)
    
    
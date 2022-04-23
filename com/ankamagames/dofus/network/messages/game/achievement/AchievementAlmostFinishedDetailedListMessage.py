from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
    


class AchievementAlmostFinishedDetailedListMessage(NetworkMessage):
    almostFinishedAchievements:list['Achievement']
    

    def init(self, almostFinishedAchievements_:list['Achievement']):
        self.almostFinishedAchievements = almostFinishedAchievements_
        
        super().__init__()
    
    
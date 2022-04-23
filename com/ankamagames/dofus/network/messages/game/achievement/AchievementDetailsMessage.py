from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
    


class AchievementDetailsMessage(NetworkMessage):
    achievement:'Achievement'
    

    def init(self, achievement_:'Achievement'):
        self.achievement = achievement_
        
        super().__init__()
    
    
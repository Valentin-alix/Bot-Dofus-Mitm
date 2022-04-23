from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
    from com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective
    


class Achievement(NetworkMessage):
    id:int
    finishedObjective:list['AchievementObjective']
    startedObjectives:list['AchievementStartedObjective']
    

    def init(self, id_:int, finishedObjective_:list['AchievementObjective'], startedObjectives_:list['AchievementStartedObjective']):
        self.id = id_
        self.finishedObjective = finishedObjective_
        self.startedObjectives = startedObjectives_
        
        super().__init__()
    
    
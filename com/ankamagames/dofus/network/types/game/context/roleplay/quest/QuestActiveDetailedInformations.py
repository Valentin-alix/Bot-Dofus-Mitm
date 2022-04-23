from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations
    


class QuestActiveDetailedInformations(QuestActiveInformations):
    stepId:int
    objectives:list['QuestObjectiveInformations']
    

    def init(self, stepId_:int, objectives_:list['QuestObjectiveInformations'], questId_:int):
        self.stepId = stepId_
        self.objectives = objectives_
        
        super().__init__(questId_)
    
    
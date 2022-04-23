from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations


class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
    curCompletion:int
    maxCompletion:int
    

    def init(self, curCompletion_:int, maxCompletion_:int, objectiveId_:int, objectiveStatus_:bool, dialogParams_:list[str]):
        self.curCompletion = curCompletion_
        self.maxCompletion = maxCompletion_
        
        super().__init__(objectiveId_, objectiveStatus_, dialogParams_)
    
    
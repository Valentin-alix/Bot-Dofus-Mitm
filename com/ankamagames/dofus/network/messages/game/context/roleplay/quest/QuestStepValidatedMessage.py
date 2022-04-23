from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestStepValidatedMessage(NetworkMessage):
    questId:int
    stepId:int
    

    def init(self, questId_:int, stepId_:int):
        self.questId = questId_
        self.stepId = stepId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FollowQuestObjectiveRequestMessage(NetworkMessage):
    questId:int
    objectiveId:int
    

    def init(self, questId_:int, objectiveId_:int):
        self.questId = questId_
        self.objectiveId = objectiveId_
        
        super().__init__()
    
    
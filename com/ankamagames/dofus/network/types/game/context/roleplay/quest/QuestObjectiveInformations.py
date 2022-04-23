from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestObjectiveInformations(NetworkMessage):
    objectiveId:int
    objectiveStatus:bool
    dialogParams:list[str]
    

    def init(self, objectiveId_:int, objectiveStatus_:bool, dialogParams_:list[str]):
        self.objectiveId = objectiveId_
        self.objectiveStatus = objectiveStatus_
        self.dialogParams = dialogParams_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayNpcQuestFlag(NetworkMessage):
    questsToValidId:list[int]
    questsToStartId:list[int]
    

    def init(self, questsToValidId_:list[int], questsToStartId_:list[int]):
        self.questsToValidId = questsToValidId_
        self.questsToStartId = questsToStartId_
        
        super().__init__()
    
    
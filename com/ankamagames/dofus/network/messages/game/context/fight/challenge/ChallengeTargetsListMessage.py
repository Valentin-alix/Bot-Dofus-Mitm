from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetsListMessage(NetworkMessage):
    targetIds:list[int]
    targetCells:list[int]
    

    def init(self, targetIds_:list[int], targetCells_:list[int]):
        self.targetIds = targetIds_
        self.targetCells = targetCells_
        
        super().__init__()
    
    
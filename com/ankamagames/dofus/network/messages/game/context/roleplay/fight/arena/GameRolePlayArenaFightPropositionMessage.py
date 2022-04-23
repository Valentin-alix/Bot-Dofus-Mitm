from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    fightId:int
    alliesId:list[int]
    duration:int
    

    def init(self, fightId_:int, alliesId_:list[int], duration_:int):
        self.fightId = fightId_
        self.alliesId = alliesId_
        self.duration = duration_
        
        super().__init__()
    
    
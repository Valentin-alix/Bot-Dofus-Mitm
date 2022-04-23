from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    

    def init(self, fightId_:int, sourceId_:int, targetId_:int, accept_:bool):
        self.fightId = fightId_
        self.sourceId = sourceId_
        self.targetId = targetId_
        self.accept = accept_
        
        super().__init__()
    
    
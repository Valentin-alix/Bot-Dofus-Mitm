from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyRequestedMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    

    def init(self, fightId_:int, sourceId_:int, targetId_:int):
        self.fightId = fightId_
        self.sourceId = sourceId_
        self.targetId = targetId_
        
        super().__init__()
    
    
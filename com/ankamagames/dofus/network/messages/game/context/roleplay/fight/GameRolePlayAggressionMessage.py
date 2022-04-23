from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayAggressionMessage(NetworkMessage):
    attackerId:int
    defenderId:int
    

    def init(self, attackerId_:int, defenderId_:int):
        self.attackerId = attackerId_
        self.defenderId = defenderId_
        
        super().__init__()
    
    
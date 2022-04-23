from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayAttackMonsterRequestMessage(NetworkMessage):
    monsterGroupId:int
    

    def init(self, monsterGroupId_:int):
        self.monsterGroupId = monsterGroupId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayMonsterNotAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    

    def init(self, playerId_:int, monsterGroupId_:int):
        self.playerId = playerId_
        self.monsterGroupId = monsterGroupId_
        
        super().__init__()
    
    
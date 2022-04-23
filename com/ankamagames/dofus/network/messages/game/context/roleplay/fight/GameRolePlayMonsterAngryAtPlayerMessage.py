from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    playerId:int
    monsterGroupId:int
    angryStartTime:int
    attackTime:int
    

    def init(self, playerId_:int, monsterGroupId_:int, angryStartTime_:int, attackTime_:int):
        self.playerId = playerId_
        self.monsterGroupId = monsterGroupId_
        self.angryStartTime = angryStartTime_
        self.attackTime = attackTime_
        
        super().__init__()
    
    
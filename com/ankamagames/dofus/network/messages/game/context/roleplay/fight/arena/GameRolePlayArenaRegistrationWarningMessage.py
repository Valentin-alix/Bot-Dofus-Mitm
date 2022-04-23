from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationWarningMessage(NetworkMessage):
    battleMode:int
    

    def init(self, battleMode_:int):
        self.battleMode = battleMode_
        
        super().__init__()
    
    
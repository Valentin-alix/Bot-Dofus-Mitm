from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    registered:bool
    step:int
    battleMode:int
    

    def init(self, registered_:bool, step_:int, battleMode_:int):
        self.registered = registered_
        self.step = step_
        self.battleMode = battleMode_
        
        super().__init__()
    
    
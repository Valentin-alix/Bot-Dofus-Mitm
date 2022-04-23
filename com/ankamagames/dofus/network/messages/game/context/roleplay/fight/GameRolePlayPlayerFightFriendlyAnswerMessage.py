from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(NetworkMessage):
    fightId:int
    accept:bool
    

    def init(self, fightId_:int, accept_:bool):
        self.fightId = fightId_
        self.accept = accept_
        
        super().__init__()
    
    
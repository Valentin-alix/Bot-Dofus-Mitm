from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    fightId:int
    teamId:int
    option:int
    state:bool
    

    def init(self, fightId_:int, teamId_:int, option_:int, state_:bool):
        self.fightId = fightId_
        self.teamId = teamId_
        self.option = option_
        self.state = state_
        
        super().__init__()
    
    
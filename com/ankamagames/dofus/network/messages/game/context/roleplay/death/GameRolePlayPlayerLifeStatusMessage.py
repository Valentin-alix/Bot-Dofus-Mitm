from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    state:int
    phenixMapId:int
    

    def init(self, state_:int, phenixMapId_:int):
        self.state = state_
        self.phenixMapId = phenixMapId_
        
        super().__init__()
    
    
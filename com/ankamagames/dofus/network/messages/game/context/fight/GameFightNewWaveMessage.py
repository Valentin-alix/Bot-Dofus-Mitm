from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    

    def init(self, id_:int, teamId_:int, nbTurnBeforeNextWave_:int):
        self.id = id_
        self.teamId = teamId_
        self.nbTurnBeforeNextWave = nbTurnBeforeNextWave_
        
        super().__init__()
    
    
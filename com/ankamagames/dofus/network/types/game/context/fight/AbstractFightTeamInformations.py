from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightTeamInformations(NetworkMessage):
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    

    def init(self, teamId_:int, leaderId_:int, teamSide_:int, teamTypeId_:int, nbWaves_:int):
        self.teamId = teamId_
        self.leaderId = leaderId_
        self.teamSide = teamSide_
        self.teamTypeId = teamTypeId_
        self.nbWaves = nbWaves_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NamedPartyTeam(NetworkMessage):
    teamId:int
    partyName:str
    

    def init(self, teamId_:int, partyName_:str):
        self.teamId = teamId_
        self.partyName = partyName_
        
        super().__init__()
    
    
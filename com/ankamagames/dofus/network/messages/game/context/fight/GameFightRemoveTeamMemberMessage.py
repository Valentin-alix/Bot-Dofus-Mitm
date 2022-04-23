from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightRemoveTeamMemberMessage(NetworkMessage):
    fightId:int
    teamId:int
    charId:int
    

    def init(self, fightId_:int, teamId_:int, charId_:int):
        self.fightId = fightId_
        self.teamId = teamId_
        self.charId = charId_
        
        super().__init__()
    
    
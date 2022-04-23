from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    fightId:int
    playerId:int
    accepted:bool
    

    def init(self, fightId_:int, playerId_:int, accepted_:bool):
        self.fightId = fightId_
        self.playerId = playerId_
        self.accepted = accepted_
        
        super().__init__()
    
    
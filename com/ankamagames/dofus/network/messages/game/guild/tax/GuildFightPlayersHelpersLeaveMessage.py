from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersLeaveMessage(NetworkMessage):
    fightId:int
    playerId:int
    

    def init(self, fightId_:int, playerId_:int):
        self.fightId = fightId_
        self.playerId = playerId_
        
        super().__init__()
    
    
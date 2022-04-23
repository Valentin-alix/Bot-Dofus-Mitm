from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationReceivedMessage(NetworkMessage):
    playerName:str
    playerId:int
    

    def init(self, playerName_:str, playerId_:int):
        self.playerName = playerName_
        self.playerId = playerId_
        
        super().__init__()
    
    
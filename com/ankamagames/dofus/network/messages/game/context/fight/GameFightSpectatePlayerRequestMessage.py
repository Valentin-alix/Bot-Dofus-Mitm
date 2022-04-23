from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightSpectatePlayerRequestMessage(NetworkMessage):
    playerId:int
    

    def init(self, playerId_:int):
        self.playerId = playerId_
        
        super().__init__()
    
    
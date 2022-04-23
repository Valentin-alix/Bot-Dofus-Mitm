from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPauseMessage(NetworkMessage):
    isPaused:bool
    

    def init(self, isPaused_:bool):
        self.isPaused = isPaused_
        
        super().__init__()
    
    
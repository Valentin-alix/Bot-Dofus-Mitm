from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightReadyMessage(NetworkMessage):
    isReady:bool
    

    def init(self, isReady_:bool):
        self.isReady = isReady_
        
        super().__init__()
    
    
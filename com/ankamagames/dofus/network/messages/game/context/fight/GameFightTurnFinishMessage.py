from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnFinishMessage(NetworkMessage):
    isAfk:bool
    

    def init(self, isAfk_:bool):
        self.isAfk = isAfk_
        
        super().__init__()
    
    
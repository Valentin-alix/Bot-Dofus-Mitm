from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnStartMessage(NetworkMessage):
    id:int
    waitTime:int
    

    def init(self, id_:int, waitTime_:int):
        self.id = id_
        self.waitTime = waitTime_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightNewRoundMessage(NetworkMessage):
    roundNumber:int
    

    def init(self, roundNumber_:int):
        self.roundNumber = roundNumber_
        
        super().__init__()
    
    
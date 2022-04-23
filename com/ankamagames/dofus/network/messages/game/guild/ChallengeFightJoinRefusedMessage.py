from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeFightJoinRefusedMessage(NetworkMessage):
    playerId:int
    reason:int
    

    def init(self, playerId_:int, reason_:int):
        self.playerId = playerId_
        self.reason = reason_
        
        super().__init__()
    
    
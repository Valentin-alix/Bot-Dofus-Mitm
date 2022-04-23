from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightJoinRequestMessage(NetworkMessage):
    fighterId:int
    fightId:int
    

    def init(self, fighterId_:int, fightId_:int):
        self.fighterId = fighterId_
        self.fightId = fightId_
        
        super().__init__()
    
    
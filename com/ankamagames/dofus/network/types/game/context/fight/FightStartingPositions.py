from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightStartingPositions(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    

    def init(self, positionsForChallengers_:list[int], positionsForDefenders_:list[int]):
        self.positionsForChallengers = positionsForChallengers_
        self.positionsForDefenders = positionsForDefenders_
        
        super().__init__()
    
    
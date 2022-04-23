from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    teamNumber:int
    

    def init(self, positionsForChallengers_:list[int], positionsForDefenders_:list[int], teamNumber_:int):
        self.positionsForChallengers = positionsForChallengers_
        self.positionsForDefenders = positionsForDefenders_
        self.teamNumber = teamNumber_
        
        super().__init__()
    
    
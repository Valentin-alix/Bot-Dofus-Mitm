from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    keyMovements:list[int]
    forcedDirection:int
    actorId:int
    

    def init(self, keyMovements_:list[int], forcedDirection_:int, actorId_:int):
        self.keyMovements = keyMovements_
        self.forcedDirection = forcedDirection_
        self.actorId = actorId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementRequestMessage(NetworkMessage):
    keyMovements:list[int]
    mapId:int
    

    def init(self, keyMovements_:list[int], mapId_:int):
        self.keyMovements = keyMovements_
        self.mapId = mapId_
        
        super().__init__()
    
    
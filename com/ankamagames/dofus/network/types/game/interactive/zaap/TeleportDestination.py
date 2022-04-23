from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportDestination(NetworkMessage):
    type:int
    mapId:int
    subAreaId:int
    level:int
    cost:int
    

    def init(self, type_:int, mapId_:int, subAreaId_:int, level_:int, cost_:int):
        self.type = type_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.level = level_
        self.cost = cost_
        
        super().__init__()
    
    
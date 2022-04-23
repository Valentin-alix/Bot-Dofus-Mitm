from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlag(NetworkMessage):
    mapId:int
    state:int
    

    def init(self, mapId_:int, state_:int):
        self.mapId = mapId_
        self.state = state_
        
        super().__init__()
    
    
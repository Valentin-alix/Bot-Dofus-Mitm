from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    mapRate:int
    subAreaRate:int
    totalRate:int
    

    def init(self, mapRate_:int, subAreaRate_:int, totalRate_:int):
        self.mapRate = mapRate_
        self.subAreaRate = subAreaRate_
        self.totalRate = totalRate_
        
        super().__init__()
    
    
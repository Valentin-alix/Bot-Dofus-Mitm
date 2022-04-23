from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ErrorMapNotFoundMessage(NetworkMessage):
    mapId:int
    

    def init(self, mapId_:int):
        self.mapId = mapId_
        
        super().__init__()
    
    
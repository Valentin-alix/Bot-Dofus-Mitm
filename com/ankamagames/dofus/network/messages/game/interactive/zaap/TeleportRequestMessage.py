from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    sourceType:int
    destinationType:int
    mapId:int
    

    def init(self, sourceType_:int, destinationType_:int, mapId_:int):
        self.sourceType = sourceType_
        self.destinationType = destinationType_
        self.mapId = mapId_
        
        super().__init__()
    
    
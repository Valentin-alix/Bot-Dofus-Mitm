from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeMapMessage(NetworkMessage):
    mapId:int
    autopilot:bool
    

    def init(self, mapId_:int, autopilot_:bool):
        self.mapId = mapId_
        self.autopilot = autopilot_
        
        super().__init__()
    
    
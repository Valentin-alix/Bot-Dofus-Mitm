from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingUpdateMessage(NetworkMessage):
    dungeonId:int
    available:bool
    

    def init(self, dungeonId_:int, available_:bool):
        self.dungeonId = dungeonId_
        self.available = available_
        
        super().__init__()
    
    
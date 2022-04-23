from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterRequestMessage(NetworkMessage):
    dungeonIds:list[int]
    

    def init(self, dungeonIds_:list[int]):
        self.dungeonIds = dungeonIds_
        
        super().__init__()
    
    
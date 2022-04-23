from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderListenErrorMessage(NetworkMessage):
    dungeonId:int
    

    def init(self, dungeonId_:int):
        self.dungeonId = dungeonId_
        
        super().__init__()
    
    
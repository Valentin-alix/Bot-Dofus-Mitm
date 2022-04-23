from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportBuddiesMessage(NetworkMessage):
    dungeonId:int
    

    def init(self, dungeonId_:int):
        self.dungeonId = dungeonId_
        
        super().__init__()
    
    
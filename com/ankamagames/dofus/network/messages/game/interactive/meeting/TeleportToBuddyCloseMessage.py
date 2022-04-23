from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyCloseMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    

    def init(self, dungeonId_:int, buddyId_:int):
        self.dungeonId = dungeonId_
        self.buddyId = buddyId_
        
        super().__init__()
    
    
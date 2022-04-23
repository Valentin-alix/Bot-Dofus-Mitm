from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    timeLeft:int
    

    def init(self, dungeonId_:int, buddyId_:int, timeLeft_:int):
        self.dungeonId = dungeonId_
        self.buddyId = buddyId_
        self.timeLeft = timeLeft_
        
        super().__init__()
    
    
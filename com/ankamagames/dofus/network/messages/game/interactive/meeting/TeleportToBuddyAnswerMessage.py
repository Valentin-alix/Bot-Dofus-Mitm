from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyAnswerMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    accept:bool
    

    def init(self, dungeonId_:int, buddyId_:int, accept_:bool):
        self.dungeonId = dungeonId_
        self.buddyId = buddyId_
        self.accept = accept_
        
        super().__init__()
    
    
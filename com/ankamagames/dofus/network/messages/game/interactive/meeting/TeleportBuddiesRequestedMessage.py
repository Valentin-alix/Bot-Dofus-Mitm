from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    dungeonId:int
    inviterId:int
    invalidBuddiesIds:list[int]
    

    def init(self, dungeonId_:int, inviterId_:int, invalidBuddiesIds_:list[int]):
        self.dungeonId = dungeonId_
        self.inviterId = inviterId_
        self.invalidBuddiesIds = invalidBuddiesIds_
        
        super().__init__()
    
    
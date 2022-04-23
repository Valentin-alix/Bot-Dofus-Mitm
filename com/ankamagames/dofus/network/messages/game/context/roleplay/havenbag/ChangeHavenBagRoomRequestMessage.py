from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeHavenBagRoomRequestMessage(NetworkMessage):
    roomId:int
    

    def init(self, roomId_:int):
        self.roomId = roomId_
        
        super().__init__()
    
    
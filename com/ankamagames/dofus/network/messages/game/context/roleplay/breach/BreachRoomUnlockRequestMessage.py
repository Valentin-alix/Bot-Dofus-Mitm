from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRoomUnlockRequestMessage(NetworkMessage):
    roomId:int
    

    def init(self, roomId_:int):
        self.roomId = roomId_
        
        super().__init__()
    
    
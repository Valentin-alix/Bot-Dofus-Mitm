from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRoomUnlockResultMessage(NetworkMessage):
    roomId:int
    result:int
    

    def init(self, roomId_:int, result_:int):
        self.roomId = roomId_
        self.result = result_
        
        super().__init__()
    
    
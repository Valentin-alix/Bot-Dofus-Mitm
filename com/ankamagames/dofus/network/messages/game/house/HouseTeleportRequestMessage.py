from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseTeleportRequestMessage(NetworkMessage):
    houseId:int
    houseInstanceId:int
    

    def init(self, houseId_:int, houseInstanceId_:int):
        self.houseId = houseId_
        self.houseInstanceId = houseInstanceId_
        
        super().__init__()
    
    
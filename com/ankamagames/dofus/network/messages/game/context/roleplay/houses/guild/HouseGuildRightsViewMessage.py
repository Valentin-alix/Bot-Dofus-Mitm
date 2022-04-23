from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildRightsViewMessage(NetworkMessage):
    houseId:int
    instanceId:int
    

    def init(self, houseId_:int, instanceId_:int):
        self.houseId = houseId_
        self.instanceId = instanceId_
        
        super().__init__()
    
    
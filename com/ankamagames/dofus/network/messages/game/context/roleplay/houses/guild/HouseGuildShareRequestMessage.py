from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    

    def init(self, houseId_:int, instanceId_:int, enable_:bool, rights_:int):
        self.houseId = houseId_
        self.instanceId = instanceId_
        self.enable = enable_
        self.rights = rights_
        
        super().__init__()
    
    
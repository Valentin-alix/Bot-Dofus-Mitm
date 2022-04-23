from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockInformations(NetworkMessage):
    maxOutdoorMount:int
    maxItems:int
    

    def init(self, maxOutdoorMount_:int, maxItems_:int):
        self.maxOutdoorMount = maxOutdoorMount_
        self.maxItems = maxItems_
        
        super().__init__()
    
    
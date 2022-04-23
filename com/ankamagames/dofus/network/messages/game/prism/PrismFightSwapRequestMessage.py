from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightSwapRequestMessage(NetworkMessage):
    subAreaId:int
    targetId:int
    

    def init(self, subAreaId_:int, targetId_:int):
        self.subAreaId = subAreaId_
        self.targetId = targetId_
        
        super().__init__()
    
    
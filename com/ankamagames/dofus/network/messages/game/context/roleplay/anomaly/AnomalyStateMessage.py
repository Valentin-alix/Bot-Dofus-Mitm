from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    subAreaId:int
    open:bool
    closingTime:int
    

    def init(self, subAreaId_:int, open_:bool, closingTime_:int):
        self.subAreaId = subAreaId_
        self.open = open_
        self.closingTime = closingTime_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSetSabotagedRefusedMessage(NetworkMessage):
    subAreaId:int
    reason:int
    

    def init(self, subAreaId_:int, reason_:int):
        self.subAreaId = subAreaId_
        self.reason = reason_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSetSabotagedRequestMessage(NetworkMessage):
    subAreaId:int
    

    def init(self, subAreaId_:int):
        self.subAreaId = subAreaId_
        
        super().__init__()
    
    
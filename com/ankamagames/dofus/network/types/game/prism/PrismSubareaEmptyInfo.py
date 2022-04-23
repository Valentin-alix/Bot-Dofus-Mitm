from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSubareaEmptyInfo(NetworkMessage):
    subAreaId:int
    allianceId:int
    

    def init(self, subAreaId_:int, allianceId_:int):
        self.subAreaId = subAreaId_
        self.allianceId = allianceId_
        
        super().__init__()
    
    
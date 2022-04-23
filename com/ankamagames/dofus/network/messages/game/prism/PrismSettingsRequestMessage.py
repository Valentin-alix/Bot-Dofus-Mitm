from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSettingsRequestMessage(NetworkMessage):
    subAreaId:int
    startDefenseTime:int
    

    def init(self, subAreaId_:int, startDefenseTime_:int):
        self.subAreaId = subAreaId_
        self.startDefenseTime = startDefenseTime_
        
        super().__init__()
    
    
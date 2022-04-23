from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AnomalySubareaInformation(NetworkMessage):
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    

    def init(self, subAreaId_:int, rewardRate_:int, hasAnomaly_:bool, anomalyClosingTime_:int):
        self.subAreaId = subAreaId_
        self.rewardRate = rewardRate_
        self.hasAnomaly = hasAnomaly_
        self.anomalyClosingTime = anomalyClosingTime_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicLatencyStatsMessage(NetworkMessage):
    latency:int
    sampleCount:int
    max:int
    

    def init(self, latency_:int, sampleCount_:int, max_:int):
        self.latency = latency_
        self.sampleCount = sampleCount_
        self.max = max_
        
        super().__init__()
    
    
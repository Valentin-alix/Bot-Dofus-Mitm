from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicTimeMessage(NetworkMessage):
    timestamp:int
    timezoneOffset:int
    

    def init(self, timestamp_:int, timezoneOffset_:int):
        self.timestamp = timestamp_
        self.timezoneOffset = timezoneOffset_
        
        super().__init__()
    
    
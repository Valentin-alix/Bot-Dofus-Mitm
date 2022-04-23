from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class OnConnectionEventMessage(NetworkMessage):
    eventType:int
    

    def init(self, eventType_:int):
        self.eventType = eventType_
        
        super().__init__()
    
    
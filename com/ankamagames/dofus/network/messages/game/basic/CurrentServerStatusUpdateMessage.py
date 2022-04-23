from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CurrentServerStatusUpdateMessage(NetworkMessage):
    status:int
    

    def init(self, status_:int):
        self.status = status_
        
        super().__init__()
    
    
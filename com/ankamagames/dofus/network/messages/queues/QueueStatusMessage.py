from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QueueStatusMessage(NetworkMessage):
    position:int
    total:int
    

    def init(self, position_:int, total_:int):
        self.position = position_
        self.total = total_
        
        super().__init__()
    
    
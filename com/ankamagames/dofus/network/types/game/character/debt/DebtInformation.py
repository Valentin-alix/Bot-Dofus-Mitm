from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebtInformation(NetworkMessage):
    id:int
    timestamp:int
    

    def init(self, id_:int, timestamp_:int):
        self.id = id_
        self.timestamp = timestamp_
        
        super().__init__()
    
    
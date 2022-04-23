from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateSelfAgressableStatusMessage(NetworkMessage):
    status:int
    probationTime:int
    

    def init(self, status_:int, probationTime_:int):
        self.status = status_
        self.probationTime = probationTime_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscription(NetworkMessage):
    jobId:int
    subscribed:bool
    

    def init(self, jobId_:int, subscribed_:bool):
        self.jobId = jobId_
        self.subscribed = subscribed_
        
        super().__init__()
    
    
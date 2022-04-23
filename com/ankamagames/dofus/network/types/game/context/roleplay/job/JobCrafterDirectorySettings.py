from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectorySettings(NetworkMessage):
    jobId:int
    minLevel:int
    free:bool
    

    def init(self, jobId_:int, minLevel_:int, free_:bool):
        self.jobId = jobId_
        self.minLevel = minLevel_
        self.free = free_
        
        super().__init__()
    
    
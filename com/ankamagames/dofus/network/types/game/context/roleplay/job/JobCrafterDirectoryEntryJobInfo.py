from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryJobInfo(NetworkMessage):
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    

    def init(self, jobId_:int, jobLevel_:int, free_:bool, minLevel_:int):
        self.jobId = jobId_
        self.jobLevel = jobLevel_
        self.free = free_
        self.minLevel = minLevel_
        
        super().__init__()
    
    
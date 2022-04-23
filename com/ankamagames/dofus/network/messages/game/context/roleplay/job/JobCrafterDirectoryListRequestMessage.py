from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryListRequestMessage(NetworkMessage):
    jobId:int
    

    def init(self, jobId_:int):
        self.jobId = jobId_
        
        super().__init__()
    
    
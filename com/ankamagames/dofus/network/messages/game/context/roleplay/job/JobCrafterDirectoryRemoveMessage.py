from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryRemoveMessage(NetworkMessage):
    jobId:int
    playerId:int
    

    def init(self, jobId_:int, playerId_:int):
        self.jobId = jobId_
        self.playerId = playerId_
        
        super().__init__()
    
    
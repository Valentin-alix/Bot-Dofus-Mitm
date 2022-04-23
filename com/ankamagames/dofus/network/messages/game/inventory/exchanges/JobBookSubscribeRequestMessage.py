from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscribeRequestMessage(NetworkMessage):
    jobIds:list[int]
    

    def init(self, jobIds_:list[int]):
        self.jobIds = jobIds_
        
        super().__init__()
    
    
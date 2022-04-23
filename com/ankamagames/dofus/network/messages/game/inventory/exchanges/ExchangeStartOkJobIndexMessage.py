from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkJobIndexMessage(NetworkMessage):
    jobs:list[int]
    

    def init(self, jobs_:list[int]):
        self.jobs = jobs_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobExperience(NetworkMessage):
    jobId:int
    jobLevel:int
    jobXP:int
    jobXpLevelFloor:int
    jobXpNextLevelFloor:int
    

    def init(self, jobId_:int, jobLevel_:int, jobXP_:int, jobXpLevelFloor_:int, jobXpNextLevelFloor_:int):
        self.jobId = jobId_
        self.jobLevel = jobLevel_
        self.jobXP = jobXP_
        self.jobXpLevelFloor = jobXpLevelFloor_
        self.jobXpNextLevelFloor = jobXpNextLevelFloor_
        
        super().__init__()
    
    
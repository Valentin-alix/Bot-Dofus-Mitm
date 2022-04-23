from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInformation(NetworkMessage):
    typeId:int
    state:int
    nextVulnerabilityDate:int
    placementDate:int
    rewardTokenCount:int
    

    def init(self, typeId_:int, state_:int, nextVulnerabilityDate_:int, placementDate_:int, rewardTokenCount_:int):
        self.typeId = typeId_
        self.state = state_
        self.nextVulnerabilityDate = nextVulnerabilityDate_
        self.placementDate = placementDate_
        self.rewardTokenCount = rewardTokenCount_
        
        super().__init__()
    
    
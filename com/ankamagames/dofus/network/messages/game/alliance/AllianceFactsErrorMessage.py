from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceFactsErrorMessage(NetworkMessage):
    allianceId:int
    

    def init(self, allianceId_:int):
        self.allianceId = allianceId_
        
        super().__init__()
    
    
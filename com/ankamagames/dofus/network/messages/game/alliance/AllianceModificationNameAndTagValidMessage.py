from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceModificationNameAndTagValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    

    def init(self, allianceName_:str, allianceTag_:str):
        self.allianceName = allianceName_
        self.allianceTag = allianceTag_
        
        super().__init__()
    
    
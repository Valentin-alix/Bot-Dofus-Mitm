from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicAllianceInformations(AbstractSocialGroupInfos):
    allianceId:int
    allianceTag:str
    

    def init(self, allianceId_:int, allianceTag_:str):
        self.allianceId = allianceId_
        self.allianceTag = allianceTag_
        
        super().__init__()
    
    
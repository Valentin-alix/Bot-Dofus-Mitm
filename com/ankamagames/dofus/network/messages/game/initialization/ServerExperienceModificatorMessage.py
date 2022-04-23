from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerExperienceModificatorMessage(NetworkMessage):
    experiencePercent:int
    

    def init(self, experiencePercent_:int):
        self.experiencePercent = experiencePercent_
        
        super().__init__()
    
    
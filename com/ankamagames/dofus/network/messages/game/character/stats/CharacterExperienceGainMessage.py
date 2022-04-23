from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    experienceCharacter:int
    experienceMount:int
    experienceGuild:int
    experienceIncarnation:int
    

    def init(self, experienceCharacter_:int, experienceMount_:int, experienceGuild_:int, experienceIncarnation_:int):
        self.experienceCharacter = experienceCharacter_
        self.experienceMount = experienceMount_
        self.experienceGuild = experienceGuild_
        self.experienceIncarnation = experienceIncarnation_
        
        super().__init__()
    
    
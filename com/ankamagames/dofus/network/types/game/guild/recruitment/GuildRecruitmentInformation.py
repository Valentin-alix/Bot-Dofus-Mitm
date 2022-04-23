from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildRecruitmentInformation(NetworkMessage):
    guildId:int
    recruitmentType:int
    recruitmentTitle:str
    recruitmentText:str
    selectedLanguages:list[int]
    selectedCriterion:list[int]
    minLevel:int
    minSuccess:int
    lastEditPlayerName:str
    lastEditDate:int
    minLevelFacultative:bool
    minSuccessFacultative:bool
    invalidatedByModeration:bool
    recruitmentAutoLocked:bool
    minLevelFacultative:bool
    minSuccessFacultative:bool
    invalidatedByModeration:bool
    recruitmentAutoLocked:bool
    

    def init(self, guildId_:int, recruitmentType_:int, recruitmentTitle_:str, recruitmentText_:str, selectedLanguages_:list[int], selectedCriterion_:list[int], minLevel_:int, minSuccess_:int, lastEditPlayerName_:str, lastEditDate_:int, minLevelFacultative_:bool, minSuccessFacultative_:bool, invalidatedByModeration_:bool, recruitmentAutoLocked_:bool):
        self.guildId = guildId_
        self.recruitmentType = recruitmentType_
        self.recruitmentTitle = recruitmentTitle_
        self.recruitmentText = recruitmentText_
        self.selectedLanguages = selectedLanguages_
        self.selectedCriterion = selectedCriterion_
        self.minLevel = minLevel_
        self.minSuccess = minSuccess_
        self.lastEditPlayerName = lastEditPlayerName_
        self.lastEditDate = lastEditDate_
        self.minLevelFacultative = minLevelFacultative_
        self.minSuccessFacultative = minSuccessFacultative_
        self.invalidatedByModeration = invalidatedByModeration_
        self.recruitmentAutoLocked = recruitmentAutoLocked_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildSubmitApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    timeSpent:int
    filterLanguage:str
    filterAmbiance:str
    filterPlaytime:str
    filterInterest:str
    filterMinMaxGuildLevel:str
    filterRecruitmentType:str
    filterMinMaxCharacterLevel:str
    filterMinMaxAchievement:str
    filterSearchName:str
    filterLastSort:str
    

    def init(self, applyText_:str, guildId_:int, timeSpent_:int, filterLanguage_:str, filterAmbiance_:str, filterPlaytime_:str, filterInterest_:str, filterMinMaxGuildLevel_:str, filterRecruitmentType_:str, filterMinMaxCharacterLevel_:str, filterMinMaxAchievement_:str, filterSearchName_:str, filterLastSort_:str):
        self.applyText = applyText_
        self.guildId = guildId_
        self.timeSpent = timeSpent_
        self.filterLanguage = filterLanguage_
        self.filterAmbiance = filterAmbiance_
        self.filterPlaytime = filterPlaytime_
        self.filterInterest = filterInterest_
        self.filterMinMaxGuildLevel = filterMinMaxGuildLevel_
        self.filterRecruitmentType = filterRecruitmentType_
        self.filterMinMaxCharacterLevel = filterMinMaxCharacterLevel_
        self.filterMinMaxAchievement = filterMinMaxAchievement_
        self.filterSearchName = filterSearchName_
        self.filterLastSort = filterLastSort_
        
        super().__init__()
    
    
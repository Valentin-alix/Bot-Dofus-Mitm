from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultExperienceData(FightResultAdditionalData):
    experience:int
    experienceLevelFloor:int
    experienceNextLevelFloor:int
    experienceFightDelta:int
    experienceForGuild:int
    experienceForMount:int
    rerollExperienceMul:int
    showExperience:bool
    showExperienceLevelFloor:bool
    showExperienceNextLevelFloor:bool
    showExperienceFightDelta:bool
    showExperienceForGuild:bool
    showExperienceForMount:bool
    isIncarnationExperience:bool
    showExperience:bool
    showExperienceLevelFloor:bool
    showExperienceNextLevelFloor:bool
    showExperienceFightDelta:bool
    showExperienceForGuild:bool
    showExperienceForMount:bool
    isIncarnationExperience:bool
    

    def init(self, experience_:int, experienceLevelFloor_:int, experienceNextLevelFloor_:int, experienceFightDelta_:int, experienceForGuild_:int, experienceForMount_:int, rerollExperienceMul_:int, showExperience_:bool, showExperienceLevelFloor_:bool, showExperienceNextLevelFloor_:bool, showExperienceFightDelta_:bool, showExperienceForGuild_:bool, showExperienceForMount_:bool, isIncarnationExperience_:bool):
        self.experience = experience_
        self.experienceLevelFloor = experienceLevelFloor_
        self.experienceNextLevelFloor = experienceNextLevelFloor_
        self.experienceFightDelta = experienceFightDelta_
        self.experienceForGuild = experienceForGuild_
        self.experienceForMount = experienceForMount_
        self.rerollExperienceMul = rerollExperienceMul_
        self.showExperience = showExperience_
        self.showExperienceLevelFloor = showExperienceLevelFloor_
        self.showExperienceNextLevelFloor = showExperienceNextLevelFloor_
        self.showExperienceFightDelta = showExperienceFightDelta_
        self.showExperienceForGuild = showExperienceForGuild_
        self.showExperienceForMount = showExperienceForMount_
        self.isIncarnationExperience = isIncarnationExperience_
        
        super().__init__()
    
    
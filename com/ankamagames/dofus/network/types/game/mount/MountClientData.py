from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
    


class MountClientData(NetworkMessage):
    id:int
    model:int
    ancestor:list[int]
    behaviors:list[int]
    name:str
    ownerId:int
    experience:int
    experienceForLevel:int
    experienceForNextLevel:int
    level:int
    maxPods:int
    stamina:int
    staminaMax:int
    maturity:int
    maturityForAdult:int
    energy:int
    energyMax:int
    serenity:int
    aggressivityMax:int
    serenityMax:int
    love:int
    loveMax:int
    fecondationTime:int
    boostLimiter:int
    boostMax:int
    reproductionCount:int
    reproductionCountMax:int
    harnessGID:int
    effectList:list['ObjectEffectInteger']
    sex:bool
    isRideable:bool
    isWild:bool
    isFecondationReady:bool
    useHarnessColors:bool
    sex:bool
    isRideable:bool
    isWild:bool
    isFecondationReady:bool
    useHarnessColors:bool
    

    def init(self, id_:int, model_:int, ancestor_:list[int], behaviors_:list[int], name_:str, ownerId_:int, experience_:int, experienceForLevel_:int, experienceForNextLevel_:int, level_:int, maxPods_:int, stamina_:int, staminaMax_:int, maturity_:int, maturityForAdult_:int, energy_:int, energyMax_:int, serenity_:int, aggressivityMax_:int, serenityMax_:int, love_:int, loveMax_:int, fecondationTime_:int, boostLimiter_:int, boostMax_:int, reproductionCount_:int, reproductionCountMax_:int, harnessGID_:int, effectList_:list['ObjectEffectInteger'], sex_:bool, isRideable_:bool, isWild_:bool, isFecondationReady_:bool, useHarnessColors_:bool):
        self.id = id_
        self.model = model_
        self.ancestor = ancestor_
        self.behaviors = behaviors_
        self.name = name_
        self.ownerId = ownerId_
        self.experience = experience_
        self.experienceForLevel = experienceForLevel_
        self.experienceForNextLevel = experienceForNextLevel_
        self.level = level_
        self.maxPods = maxPods_
        self.stamina = stamina_
        self.staminaMax = staminaMax_
        self.maturity = maturity_
        self.maturityForAdult = maturityForAdult_
        self.energy = energy_
        self.energyMax = energyMax_
        self.serenity = serenity_
        self.aggressivityMax = aggressivityMax_
        self.serenityMax = serenityMax_
        self.love = love_
        self.loveMax = loveMax_
        self.fecondationTime = fecondationTime_
        self.boostLimiter = boostLimiter_
        self.boostMax = boostMax_
        self.reproductionCount = reproductionCount_
        self.reproductionCountMax = reproductionCountMax_
        self.harnessGID = harnessGID_
        self.effectList = effectList_
        self.sex = sex_
        self.isRideable = isRideable_
        self.isWild = isWild_
        self.isFecondationReady = isFecondationReady_
        self.useHarnessColors = useHarnessColors_
        
        super().__init__()
    
    
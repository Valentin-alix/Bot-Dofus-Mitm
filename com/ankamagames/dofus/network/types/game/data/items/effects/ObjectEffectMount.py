from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
    


class ObjectEffectMount(ObjectEffect):
    id:int
    expirationDate:int
    model:int
    name:str
    owner:str
    level:int
    reproductionCount:int
    reproductionCountMax:int
    effects:list['ObjectEffectInteger']
    capacities:list[int]
    sex:bool
    isRideable:bool
    isFeconded:bool
    isFecondationReady:bool
    sex:bool
    isRideable:bool
    isFeconded:bool
    isFecondationReady:bool
    

    def init(self, id_:int, expirationDate_:int, model_:int, name_:str, owner_:str, level_:int, reproductionCount_:int, reproductionCountMax_:int, effects_:list['ObjectEffectInteger'], capacities_:list[int], sex_:bool, isRideable_:bool, isFeconded_:bool, isFecondationReady_:bool, actionId_:int):
        self.id = id_
        self.expirationDate = expirationDate_
        self.model = model_
        self.name = name_
        self.owner = owner_
        self.level = level_
        self.reproductionCount = reproductionCount_
        self.reproductionCountMax = reproductionCountMax_
        self.effects = effects_
        self.capacities = capacities_
        self.sex = sex_
        self.isRideable = isRideable_
        self.isFeconded = isFeconded_
        self.isFecondationReady = isFecondationReady_
        
        super().__init__(actionId_)
    
    
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
    deathState:int
    deathCount:int
    deathMaxLevel:int
    

    def init(self, deathState_:int, deathCount_:int, deathMaxLevel_:int, sex_:bool, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.deathState = deathState_
        self.deathCount = deathCount_
        self.deathMaxLevel = deathMaxLevel_
        
        super().__init__(sex_, entityLook_, breed_, level_, name_, id_)
    
    
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterBaseInformations(CharacterMinimalPlusLookInformations):
    sex:bool
    

    def init(self, sex_:bool, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.sex = sex_
        
        super().__init__(entityLook_, breed_, level_, name_, id_)
    
    
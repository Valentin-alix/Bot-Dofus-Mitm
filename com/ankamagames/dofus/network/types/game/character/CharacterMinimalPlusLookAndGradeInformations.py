from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalPlusLookAndGradeInformations(CharacterMinimalPlusLookInformations):
    grade:int
    

    def init(self, grade_:int, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.grade = grade_
        
        super().__init__(entityLook_, breed_, level_, name_, id_)
    
    
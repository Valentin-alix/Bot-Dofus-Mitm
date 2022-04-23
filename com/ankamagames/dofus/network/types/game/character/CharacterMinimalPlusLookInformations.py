from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
    entityLook:'EntityLook'
    breed:int
    

    def init(self, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.entityLook = entityLook_
        self.breed = breed_
        
        super().__init__(level_, name_, id_)
    
    
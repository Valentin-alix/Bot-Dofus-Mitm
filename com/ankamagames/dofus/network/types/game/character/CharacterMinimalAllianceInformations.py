from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
    alliance:'BasicAllianceInformations'
    

    def init(self, alliance_:'BasicAllianceInformations', guild_:'BasicGuildInformations', entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.alliance = alliance_
        
        super().__init__(guild_, entityLook_, breed_, level_, name_, id_)
    
    
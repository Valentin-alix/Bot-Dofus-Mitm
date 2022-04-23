from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
    sellType:int
    options:list['HumanOption']
    

    def init(self, sellType_:int, options_:list['HumanOption'], name_:str, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.sellType = sellType_
        self.options = options_
        
        super().__init__(name_, look_, contextualId_, disposition_)
    
    
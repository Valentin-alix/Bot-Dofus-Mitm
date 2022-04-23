from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
    humanoidInfo:'HumanInformations'
    accountId:int
    

    def init(self, humanoidInfo_:'HumanInformations', accountId_:int, name_:str, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.humanoidInfo = humanoidInfo_
        self.accountId = accountId_
        
        super().__init__(name_, look_, contextualId_, disposition_)
    
    
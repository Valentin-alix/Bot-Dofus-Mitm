from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
    identification:'TaxCollectorStaticInformations'
    guildLevel:int
    taxCollectorAttack:int
    

    def init(self, identification_:'TaxCollectorStaticInformations', guildLevel_:int, taxCollectorAttack_:int, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.identification = identification_
        self.guildLevel = guildLevel_
        self.taxCollectorAttack = taxCollectorAttack_
        
        super().__init__(look_, contextualId_, disposition_)
    
    
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class HumanOptionAlliance(HumanOption):
    allianceInformations:'AllianceInformations'
    aggressable:int
    

    def init(self, allianceInformations_:'AllianceInformations', aggressable_:int):
        self.allianceInformations = allianceInformations_
        self.aggressable = aggressable_
        
        super().__init__()
    
    
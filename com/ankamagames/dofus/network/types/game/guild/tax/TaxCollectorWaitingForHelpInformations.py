from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
    


class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
    waitingForHelpInfo:'ProtectedEntityWaitingForHelpInfo'
    

    def init(self, waitingForHelpInfo_:'ProtectedEntityWaitingForHelpInfo'):
        self.waitingForHelpInfo = waitingForHelpInfo_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AlliancePrismInformation(PrismInformation):
    alliance:'AllianceInformations'
    

    def init(self, alliance_:'AllianceInformations', typeId_:int, state_:int, nextVulnerabilityDate_:int, placementDate_:int, rewardTokenCount_:int):
        self.alliance = alliance_
        
        super().__init__(typeId_, state_, nextVulnerabilityDate_, placementDate_, rewardTokenCount_)
    
    
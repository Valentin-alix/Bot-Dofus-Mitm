from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
    


class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    worldX:int
    worldY:int
    mapId:int
    prism:'PrismInformation'
    

    def init(self, worldX_:int, worldY_:int, mapId_:int, prism_:'PrismInformation', subAreaId_:int, allianceId_:int):
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.prism = prism_
        
        super().__init__(subAreaId_, allianceId_)
    
    
from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.MountInformationsForPaddock import MountInformationsForPaddock
    


class PaddockContentInformations(PaddockInformations):
    paddockId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    abandonned:bool
    mountsInformations:list['MountInformationsForPaddock']
    

    def init(self, paddockId_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, abandonned_:bool, mountsInformations_:list['MountInformationsForPaddock'], maxOutdoorMount_:int, maxItems_:int):
        self.paddockId = paddockId_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.abandonned = abandonned_
        self.mountsInformations = mountsInformations_
        
        super().__init__(maxOutdoorMount_, maxItems_)
    
    
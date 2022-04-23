from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
    


class AtlasPointsInformations(NetworkMessage):
    type:int
    coords:list['MapCoordinatesExtended']
    

    def init(self, type_:int, coords_:list['MapCoordinatesExtended']):
        self.type = type_
        self.coords = coords_
        
        super().__init__()
    
    
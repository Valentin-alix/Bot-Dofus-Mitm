from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
    


class CompassUpdateMessage(NetworkMessage):
    type:int
    coords:'MapCoordinates'
    

    def init(self, type_:int, coords_:'MapCoordinates'):
        self.type = type_
        self.coords = coords_
        
        super().__init__()
    
    
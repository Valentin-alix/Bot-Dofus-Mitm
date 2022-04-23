from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
    


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    memberId:int
    active:bool
    

    def init(self, memberId_:int, active_:bool, type_:int, coords_:'MapCoordinates'):
        self.memberId = memberId_
        self.active = active_
        
        super().__init__(type_, coords_)
    
    
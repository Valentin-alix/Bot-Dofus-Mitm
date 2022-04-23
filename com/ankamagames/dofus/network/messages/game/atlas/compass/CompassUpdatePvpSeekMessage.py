from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
    


class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
    memberId:int
    memberName:str
    

    def init(self, memberId_:int, memberName_:str, type_:int, coords_:'MapCoordinates'):
        self.memberId = memberId_
        self.memberName = memberName_
        
        super().__init__(type_, coords_)
    
    
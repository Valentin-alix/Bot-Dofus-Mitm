from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation
    


class GameMapChangeOrientationsMessage(NetworkMessage):
    orientations:list['ActorOrientation']
    

    def init(self, orientations_:list['ActorOrientation']):
        self.orientations = orientations_
        
        super().__init__()
    
    
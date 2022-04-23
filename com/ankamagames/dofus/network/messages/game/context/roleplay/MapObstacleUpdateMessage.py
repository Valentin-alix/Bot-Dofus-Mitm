from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
    


class MapObstacleUpdateMessage(NetworkMessage):
    obstacles:list['MapObstacle']
    

    def init(self, obstacles_:list['MapObstacle']):
        self.obstacles = obstacles_
        
        super().__init__()
    
    
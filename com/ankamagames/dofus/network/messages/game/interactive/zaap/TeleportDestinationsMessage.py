from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination
    


class TeleportDestinationsMessage(NetworkMessage):
    type:int
    destinations:list['TeleportDestination']
    

    def init(self, type_:int, destinations_:list['TeleportDestination']):
        self.type = type_
        self.destinations = destinations_
        
        super().__init__()
    
    
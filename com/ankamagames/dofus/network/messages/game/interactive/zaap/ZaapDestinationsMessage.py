from com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import TeleportDestinationsMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination
    


class ZaapDestinationsMessage(TeleportDestinationsMessage):
    spawnMapId:int
    

    def init(self, spawnMapId_:int, type_:int, destinations_:list['TeleportDestination']):
        self.spawnMapId = spawnMapId_
        
        super().__init__(type_, destinations_)
    
    
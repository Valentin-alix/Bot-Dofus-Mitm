from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class GameContextRefreshEntityLookMessage(NetworkMessage):
    id:int
    look:'EntityLook'
    

    def init(self, id_:int, look_:'EntityLook'):
        self.id = id_
        self.look = look_
        
        super().__init__()
    
    
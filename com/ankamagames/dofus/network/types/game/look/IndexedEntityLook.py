from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class IndexedEntityLook(NetworkMessage):
    look:'EntityLook'
    index:int
    

    def init(self, look_:'EntityLook', index_:int):
        self.look = look_
        self.index = index_
        
        super().__init__()
    
    
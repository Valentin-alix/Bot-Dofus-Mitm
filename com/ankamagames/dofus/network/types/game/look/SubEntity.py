from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class SubEntity(NetworkMessage):
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:'EntityLook'
    

    def init(self, bindingPointCategory_:int, bindingPointIndex_:int, subEntityLook_:'EntityLook'):
        self.bindingPointCategory = bindingPointCategory_
        self.bindingPointIndex = bindingPointIndex_
        self.subEntityLook = subEntityLook_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyEntityBaseInformation(NetworkMessage):
    indexId:int
    entityModelId:int
    entityLook:'EntityLook'
    

    def init(self, indexId_:int, entityModelId_:int, entityLook_:'EntityLook'):
        self.indexId = indexId_
        self.entityModelId = entityModelId_
        self.entityLook = entityLook_
        
        super().__init__()
    
    
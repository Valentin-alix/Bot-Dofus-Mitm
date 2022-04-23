from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
    


class StatedElementUpdatedMessage(NetworkMessage):
    statedElement:'StatedElement'
    

    def init(self, statedElement_:'StatedElement'):
        self.statedElement = statedElement_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    


class InteractiveElementUpdatedMessage(NetworkMessage):
    interactiveElement:'InteractiveElement'
    

    def init(self, interactiveElement_:'InteractiveElement'):
        self.interactiveElement = interactiveElement_
        
        super().__init__()
    
    
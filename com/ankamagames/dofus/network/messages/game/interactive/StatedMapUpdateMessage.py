from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
    


class StatedMapUpdateMessage(NetworkMessage):
    statedElements:list['StatedElement']
    

    def init(self, statedElements_:list['StatedElement']):
        self.statedElements = statedElements_
        
        super().__init__()
    
    
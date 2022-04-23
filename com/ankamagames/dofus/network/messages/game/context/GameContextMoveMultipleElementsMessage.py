from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations
    


class GameContextMoveMultipleElementsMessage(NetworkMessage):
    movements:list['EntityMovementInformations']
    

    def init(self, movements_:list['EntityMovementInformations']):
        self.movements = movements_
        
        super().__init__()
    
    
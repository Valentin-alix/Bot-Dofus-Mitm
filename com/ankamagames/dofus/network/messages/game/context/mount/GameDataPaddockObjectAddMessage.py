from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem
    


class GameDataPaddockObjectAddMessage(NetworkMessage):
    paddockItemDescription:'PaddockItem'
    

    def init(self, paddockItemDescription_:'PaddockItem'):
        self.paddockItemDescription = paddockItemDescription_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem
    


class GameDataPaddockObjectListAddMessage(NetworkMessage):
    paddockItemDescription:list['PaddockItem']
    

    def init(self, paddockItemDescription_:list['PaddockItem']):
        self.paddockItemDescription = paddockItemDescription_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ExchangeStartedMountStockMessage(NetworkMessage):
    objectsInfos:list['ObjectItem']
    

    def init(self, objectsInfos_:list['ObjectItem']):
        self.objectsInfos = objectsInfos_
        
        super().__init__()
    
    
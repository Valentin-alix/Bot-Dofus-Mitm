from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AtlasPointsInformations import AtlasPointsInformations
    


class AtlasPointInformationsMessage(NetworkMessage):
    type:'AtlasPointsInformations'
    

    def init(self, type_:'AtlasPointsInformations'):
        self.type = type_
        
        super().__init__()
    
    
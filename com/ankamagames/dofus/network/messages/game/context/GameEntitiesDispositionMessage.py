from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
    


class GameEntitiesDispositionMessage(NetworkMessage):
    dispositions:list['IdentifiedEntityDispositionInformations']
    

    def init(self, dispositions_:list['IdentifiedEntityDispositionInformations']):
        self.dispositions = dispositions_
        
        super().__init__()
    
    
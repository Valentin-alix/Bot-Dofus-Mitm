from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameContextActorPositionInformations(NetworkMessage):
    contextualId:int
    disposition:'EntityDispositionInformations'
    

    def init(self, contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.contextualId = contextualId_
        self.disposition = disposition_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
    


class IgnoredAddedMessage(NetworkMessage):
    ignoreAdded:'IgnoredInformations'
    session:bool
    

    def init(self, ignoreAdded_:'IgnoredInformations', session_:bool):
        self.ignoreAdded = ignoreAdded_
        self.session = session_
        
        super().__init__()
    
    
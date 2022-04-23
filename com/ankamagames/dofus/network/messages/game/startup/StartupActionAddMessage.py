from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject
    


class StartupActionAddMessage(NetworkMessage):
    newAction:'StartupActionAddObject'
    

    def init(self, newAction_:'StartupActionAddObject'):
        self.newAction = newAction_
        
        super().__init__()
    
    
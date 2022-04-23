from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
    


class ShortcutBarAddRequestMessage(NetworkMessage):
    barType:int
    shortcut:'Shortcut'
    

    def init(self, barType_:int, shortcut_:'Shortcut'):
        self.barType = barType_
        self.shortcut = shortcut_
        
        super().__init__()
    
    
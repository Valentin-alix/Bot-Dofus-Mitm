from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
    


class ShortcutBarContentMessage(NetworkMessage):
    barType:int
    shortcuts:list['Shortcut']
    

    def init(self, barType_:int, shortcuts_:list['Shortcut']):
        self.barType = barType_
        self.shortcuts = shortcuts_
        
        super().__init__()
    
    
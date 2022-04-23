from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
    


class IgnoredListMessage(NetworkMessage):
    ignoredList:list['IgnoredInformations']
    

    def init(self, ignoredList_:list['IgnoredInformations']):
        self.ignoredList = ignoredList_
        
        super().__init__()
    
    
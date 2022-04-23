from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
    


class FriendAddedMessage(NetworkMessage):
    friendAdded:'FriendInformations'
    

    def init(self, friendAdded_:'FriendInformations'):
        self.friendAdded = friendAdded_
        
        super().__init__()
    
    
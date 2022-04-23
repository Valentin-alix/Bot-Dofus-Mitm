from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations
    


class SpouseInformationsMessage(NetworkMessage):
    spouse:'FriendSpouseInformations'
    

    def init(self, spouse_:'FriendSpouseInformations'):
        self.spouse = spouse_
        
        super().__init__()
    
    
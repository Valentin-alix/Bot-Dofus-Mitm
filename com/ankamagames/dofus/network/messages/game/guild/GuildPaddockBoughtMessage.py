from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations
    


class GuildPaddockBoughtMessage(NetworkMessage):
    paddockInfo:'PaddockContentInformations'
    

    def init(self, paddockInfo_:'PaddockContentInformations'):
        self.paddockInfo = paddockInfo_
        
        super().__init__()
    
    
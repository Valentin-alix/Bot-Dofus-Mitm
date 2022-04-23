from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class ServerStatusUpdateMessage(NetworkMessage):
    server:'GameServerInformations'
    

    def init(self, server_:'GameServerInformations'):
        self.server = server_
        
        super().__init__()
    
    
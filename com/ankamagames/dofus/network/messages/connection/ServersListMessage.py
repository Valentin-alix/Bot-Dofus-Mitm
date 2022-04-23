from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class ServersListMessage(NetworkMessage):
    servers:list['GameServerInformations']
    canCreateNewCharacter:bool
    

    def init(self, servers_:list['GameServerInformations'], canCreateNewCharacter_:bool):
        self.servers = servers_
        self.canCreateNewCharacter = canCreateNewCharacter_
        
        super().__init__()
    
    
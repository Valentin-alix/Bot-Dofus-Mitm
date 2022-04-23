from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import SelectedServerDataMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
    


class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    servers:list['GameServerInformations']
    

    def init(self, servers_:list['GameServerInformations'], serverId_:int, address_:str, ports_:list[int], canCreateNewCharacter_:bool, ticket_:list[int]):
        self.servers = servers_
        
        super().__init__(serverId_, address_, ports_, canCreateNewCharacter_, ticket_)
    
    
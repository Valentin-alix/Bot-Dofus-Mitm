from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerDataMessage(NetworkMessage):
    serverId:int
    address:str
    ports:list[int]
    canCreateNewCharacter:bool
    ticket:list[int]
    

    def init(self, serverId_:int, address_:str, ports_:list[int], canCreateNewCharacter_:bool, ticket_:list[int]):
        self.serverId = serverId_
        self.address = address_
        self.ports = ports_
        self.canCreateNewCharacter = canCreateNewCharacter_
        self.ticket = ticket_
        
        super().__init__()
    
    
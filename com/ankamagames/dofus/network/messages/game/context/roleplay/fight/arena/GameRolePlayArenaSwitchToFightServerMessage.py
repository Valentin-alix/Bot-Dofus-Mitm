from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    address:str
    ports:list[int]
    ticket:list[int]
    

    def init(self, address_:str, ports_:list[int], ticket_:list[int]):
        self.address = address_
        self.ports = ports_
        self.ticket = ticket_
        
        super().__init__()
    
    
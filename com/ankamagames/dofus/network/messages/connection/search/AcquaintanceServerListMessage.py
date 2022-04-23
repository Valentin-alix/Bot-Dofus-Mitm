from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AcquaintanceServerListMessage(NetworkMessage):
    servers:list[int]
    

    def init(self, servers_:list[int]):
        self.servers = servers_
        
        super().__init__()
    
    
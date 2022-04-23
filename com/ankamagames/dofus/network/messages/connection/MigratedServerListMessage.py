from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MigratedServerListMessage(NetworkMessage):
    migratedServerIds:list[int]
    

    def init(self, migratedServerIds_:list[int]):
        self.migratedServerIds = migratedServerIds_
        
        super().__init__()
    
    
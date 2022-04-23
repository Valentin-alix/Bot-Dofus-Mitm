from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSelectionMessage(NetworkMessage):
    serverId:int
    

    def init(self, serverId_:int):
        self.serverId = serverId_
        
        super().__init__()
    
    
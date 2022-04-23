from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    serverId:int
    error:int
    serverStatus:int
    

    def init(self, serverId_:int, error_:int, serverStatus_:int):
        self.serverId = serverId_
        self.error = error_
        self.serverStatus = serverStatus_
        
        super().__init__()
    
    
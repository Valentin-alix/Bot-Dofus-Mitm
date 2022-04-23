from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicPingMessage(NetworkMessage):
    quiet:bool
    

    def init(self, quiet_:bool):
        self.quiet = quiet_
        
        super().__init__()
    
    
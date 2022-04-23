from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobAllowMultiCraftRequestMessage(NetworkMessage):
    enabled:bool
    

    def init(self, enabled_:bool):
        self.enabled = enabled_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SetEnableAVARequestMessage(NetworkMessage):
    enable:bool
    

    def init(self, enable_:bool):
        self.enable = enable_
        
        super().__init__()
    
    
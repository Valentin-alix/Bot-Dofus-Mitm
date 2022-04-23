from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FriendSetWarnOnLevelGainMessage(NetworkMessage):
    enable:bool
    

    def init(self, enable_:bool):
        self.enable = enable_
        
        super().__init__()
    
    
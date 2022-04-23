from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChannelEnablingMessage(NetworkMessage):
    channel:int
    enable:bool
    

    def init(self, channel_:int, enable_:bool):
        self.channel = channel_
        self.enable = enable_
        
        super().__init__()
    
    
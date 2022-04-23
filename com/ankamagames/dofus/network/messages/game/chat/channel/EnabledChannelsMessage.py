from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    channels:list[int]
    disallowed:list[int]
    

    def init(self, channels_:list[int], disallowed_:list[int]):
        self.channels = channels_
        self.disallowed = disallowed_
        
        super().__init__()
    
    
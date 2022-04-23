from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    channel:int
    content:str
    timestamp:int
    fingerprint:str
    

    def init(self, channel_:int, content_:str, timestamp_:int, fingerprint_:str):
        self.channel = channel_
        self.content = content_
        self.timestamp = timestamp_
        self.fingerprint = fingerprint_
        
        super().__init__()
    
    
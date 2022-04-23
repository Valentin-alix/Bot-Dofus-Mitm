from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RawDataMessage(NetworkMessage):
    content:bytearray
    

    def init(self, content_:bytearray):
        self.content = content_
        
        super().__init__()
    
    
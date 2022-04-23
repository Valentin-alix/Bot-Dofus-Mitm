from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ProtocolRequired(NetworkMessage):
    version:str
    

    def init(self, version_:str):
        self.version = version_
        
        super().__init__()
    
    
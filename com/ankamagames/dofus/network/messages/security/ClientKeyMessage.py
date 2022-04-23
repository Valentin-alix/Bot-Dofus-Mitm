from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ClientKeyMessage(NetworkMessage):
    key:str
    

    def init(self, key_:str):
        self.key = key_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    salt:str
    key:list[int]
    

    def init(self, salt_:str, key_:list[int]):
        self.salt = salt_
        self.key = key_
        
        super().__init__()
    
    
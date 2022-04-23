from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiApiKeyMessage(NetworkMessage):
    token:str
    

    def init(self, token_:str):
        self.token = token_
        
        super().__init__()
    
    
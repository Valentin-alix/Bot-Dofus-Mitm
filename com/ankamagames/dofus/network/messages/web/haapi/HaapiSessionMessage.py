from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiSessionMessage(NetworkMessage):
    key:str
    type:int
    

    def init(self, key_:str, type_:int):
        self.key = key_
        self.type = type_
        
        super().__init__()
    
    
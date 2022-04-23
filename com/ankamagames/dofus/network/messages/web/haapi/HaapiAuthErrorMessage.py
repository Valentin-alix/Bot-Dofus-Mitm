from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiAuthErrorMessage(NetworkMessage):
    type:int
    

    def init(self, type_:int):
        self.type = type_
        
        super().__init__()
    
    
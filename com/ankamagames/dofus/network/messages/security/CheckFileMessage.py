from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    filenameHash:str
    type:int
    value:str
    

    def init(self, filenameHash_:str, type_:int, value_:str):
        self.filenameHash = filenameHash_
        self.type = type_
        self.value = value_
        
        super().__init__()
    
    
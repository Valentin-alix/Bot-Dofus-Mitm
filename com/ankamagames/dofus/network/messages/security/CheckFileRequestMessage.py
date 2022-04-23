from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileRequestMessage(NetworkMessage):
    filename:str
    type:int
    

    def init(self, filename_:str, type_:int):
        self.filename = filename_
        self.type = type_
        
        super().__init__()
    
    
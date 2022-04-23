from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableChangeCodeMessage(NetworkMessage):
    code:str
    

    def init(self, code_:str):
        self.code = code_
        
        super().__init__()
    
    
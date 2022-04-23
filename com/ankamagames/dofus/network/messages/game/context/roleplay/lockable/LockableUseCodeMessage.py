from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableUseCodeMessage(NetworkMessage):
    code:str
    

    def init(self, code_:str):
        self.code = code_
        
        super().__init__()
    
    
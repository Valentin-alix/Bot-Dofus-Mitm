from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    accountId:int
    session:bool
    

    def init(self, accountId_:int, session_:bool):
        self.accountId = accountId_
        self.session = session_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectMessage(NetworkMessage):
    remote:bool
    

    def init(self, remote_:bool):
        self.remote = remote_
        
        super().__init__()
    
    
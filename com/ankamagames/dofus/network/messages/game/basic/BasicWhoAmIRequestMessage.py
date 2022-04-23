from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicWhoAmIRequestMessage(NetworkMessage):
    verbose:bool
    

    def init(self, verbose_:bool):
        self.verbose = verbose_
        
        super().__init__()
    
    
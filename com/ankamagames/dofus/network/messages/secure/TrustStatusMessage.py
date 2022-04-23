from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TrustStatusMessage(NetworkMessage):
    trusted:bool
    certified:bool
    trusted:bool
    certified:bool
    

    def init(self, trusted_:bool, certified_:bool):
        self.trusted = trusted_
        self.certified = certified_
        
        super().__init__()
    
    
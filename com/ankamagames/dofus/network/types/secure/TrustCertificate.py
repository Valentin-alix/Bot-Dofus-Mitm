from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TrustCertificate(NetworkMessage):
    id:int
    hash:str
    

    def init(self, id_:int, hash_:str):
        self.id = id_
        self.hash = hash_
        
        super().__init__()
    
    
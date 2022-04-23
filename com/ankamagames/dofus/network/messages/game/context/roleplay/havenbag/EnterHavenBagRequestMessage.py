from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EnterHavenBagRequestMessage(NetworkMessage):
    havenBagOwner:int
    

    def init(self, havenBagOwner_:int):
        self.havenBagOwner = havenBagOwner_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class KickHavenBagRequestMessage(NetworkMessage):
    guestId:int
    

    def init(self, guestId_:int):
        self.guestId = guestId_
        
        super().__init__()
    
    
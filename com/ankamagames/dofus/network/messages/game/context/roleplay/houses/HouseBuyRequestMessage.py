from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseBuyRequestMessage(NetworkMessage):
    proposedPrice:int
    

    def init(self, proposedPrice_:int):
        self.proposedPrice = proposedPrice_
        
        super().__init__()
    
    
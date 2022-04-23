from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyRequestMessage(NetworkMessage):
    proposedPrice:int
    

    def init(self, proposedPrice_:int):
        self.proposedPrice = proposedPrice_
        
        super().__init__()
    
    
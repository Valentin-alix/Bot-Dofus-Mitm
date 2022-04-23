from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeWeightMessage(NetworkMessage):
    currentWeight:int
    maxWeight:int
    

    def init(self, currentWeight_:int, maxWeight_:int):
        self.currentWeight = currentWeight_
        self.maxWeight = maxWeight_
        
        super().__init__()
    
    
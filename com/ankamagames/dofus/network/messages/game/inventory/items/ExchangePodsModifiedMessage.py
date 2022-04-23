from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    currentWeight:int
    maxWeight:int
    

    def init(self, currentWeight_:int, maxWeight_:int, remote_:bool):
        self.currentWeight = currentWeight_
        self.maxWeight = maxWeight_
        
        super().__init__(remote_)
    
    
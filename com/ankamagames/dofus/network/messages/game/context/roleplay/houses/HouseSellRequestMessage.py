from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    instanceId:int
    amount:int
    forSale:bool
    

    def init(self, instanceId_:int, amount_:int, forSale_:bool):
        self.instanceId = instanceId_
        self.amount = amount_
        self.forSale = forSale_
        
        super().__init__()
    
    
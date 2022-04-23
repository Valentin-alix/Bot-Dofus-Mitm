from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseBuyResultMessage(NetworkMessage):
    houseId:int
    instanceId:int
    realPrice:int
    secondHand:bool
    bought:bool
    secondHand:bool
    bought:bool
    

    def init(self, houseId_:int, instanceId_:int, realPrice_:int, secondHand_:bool, bought_:bool):
        self.houseId = houseId_
        self.instanceId = instanceId_
        self.realPrice = realPrice_
        self.secondHand = secondHand_
        self.bought = bought_
        
        super().__init__()
    
    
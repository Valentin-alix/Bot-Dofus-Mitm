from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbMount:int
    atLeastNbMachine:int
    maxPrice:int
    orderBy:int
    

    def init(self, areaId_:int, atLeastNbMount_:int, atLeastNbMachine_:int, maxPrice_:int, orderBy_:int):
        self.areaId = areaId_
        self.atLeastNbMount = atLeastNbMount_
        self.atLeastNbMachine = atLeastNbMachine_
        self.maxPrice = maxPrice_
        self.orderBy = orderBy_
        
        super().__init__()
    
    
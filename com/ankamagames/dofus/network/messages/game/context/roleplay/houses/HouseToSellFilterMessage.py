from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:int
    orderBy:int
    

    def init(self, areaId_:int, atLeastNbRoom_:int, atLeastNbChest_:int, skillRequested_:int, maxPrice_:int, orderBy_:int):
        self.areaId = areaId_
        self.atLeastNbRoom = atLeastNbRoom_
        self.atLeastNbChest = atLeastNbChest_
        self.skillRequested = skillRequested_
        self.maxPrice = maxPrice_
        self.orderBy = orderBy_
        
        super().__init__()
    
    
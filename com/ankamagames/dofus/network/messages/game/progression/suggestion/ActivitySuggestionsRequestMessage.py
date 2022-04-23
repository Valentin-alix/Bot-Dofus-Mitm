from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsRequestMessage(NetworkMessage):
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    

    def init(self, minLevel_:int, maxLevel_:int, areaId_:int, activityCategoryId_:int, nbCards_:int):
        self.minLevel = minLevel_
        self.maxLevel = maxLevel_
        self.areaId = areaId_
        self.activityCategoryId = activityCategoryId_
        self.nbCards = nbCards_
        
        super().__init__()
    
    
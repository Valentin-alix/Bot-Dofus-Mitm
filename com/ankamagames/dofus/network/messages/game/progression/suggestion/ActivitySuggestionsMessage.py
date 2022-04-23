from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsMessage(NetworkMessage):
    lockedActivitiesIds:list[int]
    unlockedActivitiesIds:list[int]
    

    def init(self, lockedActivitiesIds_:list[int], unlockedActivitiesIds_:list[int]):
        self.lockedActivitiesIds = lockedActivitiesIds_
        self.unlockedActivitiesIds = unlockedActivitiesIds_
        
        super().__init__()
    
    
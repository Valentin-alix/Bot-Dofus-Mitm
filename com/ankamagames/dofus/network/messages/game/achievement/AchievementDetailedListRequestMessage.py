from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementDetailedListRequestMessage(NetworkMessage):
    categoryId:int
    

    def init(self, categoryId_:int):
        self.categoryId = categoryId_
        
        super().__init__()
    
    
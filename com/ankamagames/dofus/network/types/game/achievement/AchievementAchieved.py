from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementAchieved(NetworkMessage):
    id:int
    achievedBy:int
    

    def init(self, id_:int, achievedBy_:int):
        self.id = id_
        self.achievedBy = achievedBy_
        
        super().__init__()
    
    
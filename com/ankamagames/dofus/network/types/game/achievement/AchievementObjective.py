from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementObjective(NetworkMessage):
    id:int
    maxValue:int
    

    def init(self, id_:int, maxValue_:int):
        self.id = id_
        self.maxValue = maxValue_
        
        super().__init__()
    
    
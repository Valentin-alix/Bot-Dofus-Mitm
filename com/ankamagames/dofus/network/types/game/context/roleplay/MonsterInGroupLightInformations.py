from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MonsterInGroupLightInformations(NetworkMessage):
    genericId:int
    grade:int
    level:int
    

    def init(self, genericId_:int, grade_:int, level_:int):
        self.genericId = genericId_
        self.grade = grade_
        self.level = level_
        
        super().__init__()
    
    
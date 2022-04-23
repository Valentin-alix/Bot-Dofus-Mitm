from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveElementSkill(NetworkMessage):
    skillId:int
    skillInstanceUid:int
    

    def init(self, skillId_:int, skillInstanceUid_:int):
        self.skillId = skillId_
        self.skillInstanceUid = skillInstanceUid_
        
        super().__init__()
    
    
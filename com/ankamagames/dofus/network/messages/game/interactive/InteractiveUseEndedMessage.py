from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUseEndedMessage(NetworkMessage):
    elemId:int
    skillId:int
    

    def init(self, elemId_:int, skillId_:int):
        self.elemId = elemId_
        self.skillId = skillId_
        
        super().__init__()
    
    
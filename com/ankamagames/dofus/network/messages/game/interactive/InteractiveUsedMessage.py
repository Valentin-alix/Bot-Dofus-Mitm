from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    

    def init(self, entityId_:int, elemId_:int, skillId_:int, duration_:int, canMove_:bool):
        self.entityId = entityId_
        self.elemId = elemId_
        self.skillId = skillId_
        self.duration = duration_
        self.canMove = canMove_
        
        super().__init__()
    
    
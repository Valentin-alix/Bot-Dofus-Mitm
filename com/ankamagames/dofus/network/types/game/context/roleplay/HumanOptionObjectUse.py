from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionObjectUse(HumanOption):
    delayTypeId:int
    delayEndTime:int
    objectGID:int
    

    def init(self, delayTypeId_:int, delayEndTime_:int, objectGID_:int):
        self.delayTypeId = delayTypeId_
        self.delayEndTime = delayEndTime_
        self.objectGID = objectGID_
        
        super().__init__()
    
    
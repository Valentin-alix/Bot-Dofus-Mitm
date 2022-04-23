from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    

    def init(self, houseId_:int, instanceId_:int, secondHand_:bool, locked_:bool):
        self.houseId = houseId_
        self.instanceId = instanceId_
        self.secondHand = secondHand_
        
        super().__init__(locked_)
    
    
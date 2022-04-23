from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    mapId:int
    elementId:int
    

    def init(self, mapId_:int, elementId_:int, locked_:bool):
        self.mapId = mapId_
        self.elementId = elementId_
        
        super().__init__(locked_)
    
    
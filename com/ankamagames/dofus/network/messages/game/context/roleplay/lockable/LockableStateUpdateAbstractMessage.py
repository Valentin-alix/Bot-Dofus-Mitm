from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableStateUpdateAbstractMessage(NetworkMessage):
    locked:bool
    

    def init(self, locked_:bool):
        self.locked = locked_
        
        super().__init__()
    
    
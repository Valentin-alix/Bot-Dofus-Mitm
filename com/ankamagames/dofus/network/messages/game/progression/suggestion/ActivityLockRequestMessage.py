from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivityLockRequestMessage(NetworkMessage):
    activityId:int
    lock:bool
    

    def init(self, activityId_:int, lock_:bool):
        self.activityId = activityId_
        self.lock = lock_
        
        super().__init__()
    
    
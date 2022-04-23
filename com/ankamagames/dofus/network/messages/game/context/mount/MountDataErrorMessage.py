from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountDataErrorMessage(NetworkMessage):
    reason:int
    

    def init(self, reason_:int):
        self.reason = reason_
        
        super().__init__()
    
    
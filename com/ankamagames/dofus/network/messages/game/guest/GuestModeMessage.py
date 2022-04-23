from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuestModeMessage(NetworkMessage):
    active:bool
    

    def init(self, active_:bool):
        self.active = active_
        
        super().__init__()
    
    
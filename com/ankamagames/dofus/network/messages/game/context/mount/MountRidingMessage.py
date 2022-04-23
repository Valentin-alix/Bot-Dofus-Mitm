from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRidingMessage(NetworkMessage):
    isRiding:bool
    isAutopilot:bool
    isRiding:bool
    isAutopilot:bool
    

    def init(self, isRiding_:bool, isAutopilot_:bool):
        self.isRiding = isRiding_
        self.isAutopilot = isAutopilot_
        
        super().__init__()
    
    
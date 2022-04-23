from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachKickRequestMessage(NetworkMessage):
    target:int
    

    def init(self, target_:int):
        self.target = target_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachExitResponseMessage(NetworkMessage):
    exited:bool
    

    def init(self, exited_:bool):
        self.exited = exited_
        
        super().__init__()
    
    
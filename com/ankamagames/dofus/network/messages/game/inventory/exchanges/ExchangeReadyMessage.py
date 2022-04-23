from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeReadyMessage(NetworkMessage):
    ready:bool
    step:int
    

    def init(self, ready_:bool, step_:int):
        self.ready = ready_
        self.step = step_
        
        super().__init__()
    
    
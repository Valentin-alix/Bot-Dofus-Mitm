from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachBudgetMessage(NetworkMessage):
    bugdet:int
    

    def init(self, bugdet_:int):
        self.bugdet = bugdet_
        
        super().__init__()
    
    
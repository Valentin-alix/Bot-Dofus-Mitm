from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorStateUpdateMessage(NetworkMessage):
    uniqueId:int
    state:int
    

    def init(self, uniqueId_:int, state_:int):
        self.uniqueId = uniqueId_
        self.state = state_
        
        super().__init__()
    
    
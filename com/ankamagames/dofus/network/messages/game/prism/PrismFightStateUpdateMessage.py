from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightStateUpdateMessage(NetworkMessage):
    state:int
    

    def init(self, state_:int):
        self.state = state_
        
        super().__init__()
    
    
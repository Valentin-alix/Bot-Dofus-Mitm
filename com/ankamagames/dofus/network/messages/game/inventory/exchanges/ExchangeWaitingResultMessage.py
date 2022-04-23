from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeWaitingResultMessage(NetworkMessage):
    bwait:bool
    

    def init(self, bwait_:bool):
        self.bwait = bwait_
        
        super().__init__()
    
    
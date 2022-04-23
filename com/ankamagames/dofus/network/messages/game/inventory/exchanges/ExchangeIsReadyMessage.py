from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeIsReadyMessage(NetworkMessage):
    id:int
    ready:bool
    

    def init(self, id_:int, ready_:bool):
        self.id = id_
        self.ready = ready_
        
        super().__init__()
    
    
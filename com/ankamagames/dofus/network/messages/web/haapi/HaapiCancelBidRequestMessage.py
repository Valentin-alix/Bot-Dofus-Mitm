from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiCancelBidRequestMessage(NetworkMessage):
    id:int
    type:int
    

    def init(self, id_:int, type_:int):
        self.id = id_
        self.type = type_
        
        super().__init__()
    
    
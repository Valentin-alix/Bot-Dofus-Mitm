from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BufferInformation(NetworkMessage):
    id:int
    amount:int
    

    def init(self, id_:int, amount_:int):
        self.id = id_
        self.amount = amount_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RecycledItem(NetworkMessage):
    id:int
    qty:int
    

    def init(self, id_:int, qty_:int):
        self.id = id_
        self.qty = qty_
        
        super().__init__()
    
    
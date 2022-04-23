from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    uid:int
    qty:int
    price:int
    

    def init(self, uid_:int, qty_:int, price_:int):
        self.uid = uid_
        self.qty = qty_
        self.price = price_
        
        super().__init__()
    
    
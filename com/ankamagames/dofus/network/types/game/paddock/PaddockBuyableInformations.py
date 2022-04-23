from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyableInformations(NetworkMessage):
    price:int
    locked:bool
    

    def init(self, price_:int, locked_:bool):
        self.price = price_
        self.locked = locked_
        
        super().__init__()
    
    
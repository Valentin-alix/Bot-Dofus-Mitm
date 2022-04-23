from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    price:int
    forSale:bool
    

    def init(self, price_:int, forSale_:bool):
        self.price = price_
        self.forSale = forSale_
        
        super().__init__()
    
    
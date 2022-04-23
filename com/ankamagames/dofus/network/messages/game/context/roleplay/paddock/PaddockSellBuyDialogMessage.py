from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellBuyDialogMessage(NetworkMessage):
    bsell:bool
    ownerId:int
    price:int
    

    def init(self, bsell_:bool, ownerId_:int, price_:int):
        self.bsell = bsell_
        self.ownerId = ownerId_
        self.price = price_
        
        super().__init__()
    
    
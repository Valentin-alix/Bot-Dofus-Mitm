from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    purchasableId:int
    purchasableInstanceId:int
    price:int
    buyOrSell:bool
    secondHand:bool
    buyOrSell:bool
    secondHand:bool
    

    def init(self, purchasableId_:int, purchasableInstanceId_:int, price_:int, buyOrSell_:bool, secondHand_:bool):
        self.purchasableId = purchasableId_
        self.purchasableInstanceId = purchasableInstanceId_
        self.price = price_
        self.buyOrSell = buyOrSell_
        self.secondHand = secondHand_
        
        super().__init__()
    
    
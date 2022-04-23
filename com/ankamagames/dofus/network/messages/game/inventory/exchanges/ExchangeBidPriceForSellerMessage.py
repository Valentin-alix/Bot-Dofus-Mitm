from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage


class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    allIdentical:bool
    minimalPrices:list[int]
    

    def init(self, allIdentical_:bool, minimalPrices_:list[int], genericId_:int, averagePrice_:int):
        self.allIdentical = allIdentical_
        self.minimalPrices = minimalPrices_
        
        super().__init__(genericId_, averagePrice_)
    
    
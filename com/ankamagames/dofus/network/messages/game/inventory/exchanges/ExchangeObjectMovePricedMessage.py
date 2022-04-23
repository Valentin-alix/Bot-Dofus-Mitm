from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage


class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
    price:int
    

    def init(self, price_:int, objectUID_:int, quantity_:int):
        self.price = price_
        
        super().__init__(objectUID_, quantity_)
    
    
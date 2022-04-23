from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage


class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    source:int
    target:int
    

    def init(self, source_:int, target_:int, exchangeType_:int):
        self.source = source_
        self.target = target_
        
        super().__init__(exchangeType_)
    
    
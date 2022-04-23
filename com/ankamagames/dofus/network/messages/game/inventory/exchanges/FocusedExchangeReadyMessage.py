from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReadyMessage import ExchangeReadyMessage


class FocusedExchangeReadyMessage(ExchangeReadyMessage):
    focusActionId:int
    

    def init(self, focusActionId_:int, ready_:bool, step_:int):
        self.focusActionId = focusActionId_
        
        super().__init__(ready_, step_)
    
    
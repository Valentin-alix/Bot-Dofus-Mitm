from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage


class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
    objectGenericId:int
    

    def init(self, objectGenericId_:int, craftResult_:int):
        self.objectGenericId = objectGenericId_
        
        super().__init__(craftResult_)
    
    
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    target:int
    skillId:int
    

    def init(self, target_:int, skillId_:int, exchangeType_:int):
        self.target = target_
        self.skillId = skillId_
        
        super().__init__(exchangeType_)
    
    
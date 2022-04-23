from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage


class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
    skillId:int
    

    def init(self, skillId_:int):
        self.skillId = skillId_
        
        super().__init__()
    
    
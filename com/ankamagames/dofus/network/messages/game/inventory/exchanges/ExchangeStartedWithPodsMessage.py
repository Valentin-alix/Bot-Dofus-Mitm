from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    firstCharacterId:int
    firstCharacterCurrentWeight:int
    firstCharacterMaxWeight:int
    secondCharacterId:int
    secondCharacterCurrentWeight:int
    secondCharacterMaxWeight:int
    

    def init(self, firstCharacterId_:int, firstCharacterCurrentWeight_:int, firstCharacterMaxWeight_:int, secondCharacterId_:int, secondCharacterCurrentWeight_:int, secondCharacterMaxWeight_:int, exchangeType_:int):
        self.firstCharacterId = firstCharacterId_
        self.firstCharacterCurrentWeight = firstCharacterCurrentWeight_
        self.firstCharacterMaxWeight = firstCharacterMaxWeight_
        self.secondCharacterId = secondCharacterId_
        self.secondCharacterCurrentWeight = secondCharacterCurrentWeight_
        self.secondCharacterMaxWeight = secondCharacterMaxWeight_
        
        super().__init__(exchangeType_)
    
    
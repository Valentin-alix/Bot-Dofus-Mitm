from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage


class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
    wrongFlagCount:int
    

    def init(self, wrongFlagCount_:int, questType_:int, result_:int):
        self.wrongFlagCount = wrongFlagCount_
        
        super().__init__(questType_, result_)
    
    
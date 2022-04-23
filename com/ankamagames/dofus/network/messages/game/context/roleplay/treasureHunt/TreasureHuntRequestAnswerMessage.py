from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntRequestAnswerMessage(NetworkMessage):
    questType:int
    result:int
    

    def init(self, questType_:int, result_:int):
        self.questType = questType_
        self.result = result_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestAnswerMessage(NetworkMessage):
    questType:int
    result:int
    index:int
    

    def init(self, questType_:int, result_:int, index_:int):
        self.questType = questType_
        self.result = result_
        self.index = index_
        
        super().__init__()
    
    
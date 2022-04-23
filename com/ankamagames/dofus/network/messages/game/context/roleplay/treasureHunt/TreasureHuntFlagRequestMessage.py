from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestMessage(NetworkMessage):
    questType:int
    index:int
    

    def init(self, questType_:int, index_:int):
        self.questType = questType_
        self.index = index_
        
        super().__init__()
    
    
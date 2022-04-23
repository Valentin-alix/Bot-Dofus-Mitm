from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestMessage(NetworkMessage):
    questType:int
    

    def init(self, questType_:int):
        self.questType = questType_
        
        super().__init__()
    
    
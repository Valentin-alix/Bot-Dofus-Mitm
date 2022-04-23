from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntGiveUpRequestMessage(NetworkMessage):
    questType:int
    

    def init(self, questType_:int):
        self.questType = questType_
        
        super().__init__()
    
    
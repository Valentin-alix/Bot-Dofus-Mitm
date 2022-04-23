from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(NetworkMessage):
    questType:int
    availableRetryCount:int
    

    def init(self, questType_:int, availableRetryCount_:int):
        self.questType = questType_
        self.availableRetryCount = availableRetryCount_
        
        super().__init__()
    
    
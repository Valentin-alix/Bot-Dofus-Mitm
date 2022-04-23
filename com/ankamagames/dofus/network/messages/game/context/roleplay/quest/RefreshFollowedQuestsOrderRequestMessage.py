from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(NetworkMessage):
    quests:list[int]
    

    def init(self, quests_:list[int]):
        self.quests = quests_
        
        super().__init__()
    
    
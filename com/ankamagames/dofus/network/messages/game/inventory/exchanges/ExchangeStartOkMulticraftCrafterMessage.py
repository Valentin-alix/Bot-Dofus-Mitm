from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(NetworkMessage):
    skillId:int
    

    def init(self, skillId_:int):
        self.skillId = skillId_
        
        super().__init__()
    
    
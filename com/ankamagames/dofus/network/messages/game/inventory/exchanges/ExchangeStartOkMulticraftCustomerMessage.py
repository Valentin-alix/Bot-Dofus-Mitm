from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(NetworkMessage):
    skillId:int
    crafterJobLevel:int
    

    def init(self, skillId_:int, crafterJobLevel_:int):
        self.skillId = skillId_
        self.crafterJobLevel = crafterJobLevel_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeOkMultiCraftMessage(NetworkMessage):
    initiatorId:int
    otherId:int
    role:int
    

    def init(self, initiatorId_:int, otherId_:int, role_:int):
        self.initiatorId = initiatorId_
        self.otherId = otherId_
        self.role = role_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeHandleMountsMessage(NetworkMessage):
    actionType:int
    ridesId:list[int]
    

    def init(self, actionType_:int, ridesId_:list[int]):
        self.actionType = actionType_
        self.ridesId = ridesId_
        
        super().__init__()
    
    
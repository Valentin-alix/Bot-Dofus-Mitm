from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMoneyMovementInformationMessage(NetworkMessage):
    limit:int
    

    def init(self, limit_:int):
        self.limit = limit_
        
        super().__init__()
    
    
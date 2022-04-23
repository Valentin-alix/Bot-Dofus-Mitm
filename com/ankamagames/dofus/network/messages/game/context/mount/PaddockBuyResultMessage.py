from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyResultMessage(NetworkMessage):
    paddockId:int
    bought:bool
    realPrice:int
    

    def init(self, paddockId_:int, bought_:bool, realPrice_:int):
        self.paddockId = paddockId_
        self.bought = bought_
        self.realPrice = realPrice_
        
        super().__init__()
    
    
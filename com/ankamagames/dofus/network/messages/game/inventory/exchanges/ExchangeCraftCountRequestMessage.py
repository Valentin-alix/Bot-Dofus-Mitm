from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftCountRequestMessage(NetworkMessage):
    count:int
    

    def init(self, count_:int):
        self.count = count_
        
        super().__init__()
    
    
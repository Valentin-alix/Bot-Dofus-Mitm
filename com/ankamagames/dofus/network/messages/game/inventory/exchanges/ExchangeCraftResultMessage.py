from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCraftResultMessage(NetworkMessage):
    craftResult:int
    

    def init(self, craftResult_:int):
        self.craftResult = craftResult_
        
        super().__init__()
    
    
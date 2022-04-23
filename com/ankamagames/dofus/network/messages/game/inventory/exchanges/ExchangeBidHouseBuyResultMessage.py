from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyResultMessage(NetworkMessage):
    uid:int
    bought:bool
    

    def init(self, uid_:int, bought_:bool):
        self.uid = uid_
        self.bought = bought_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRewardBoughtMessage(NetworkMessage):
    id:int
    bought:bool
    

    def init(self, id_:int, bought_:bool):
        self.id = id_
        self.bought = bought_
        
        super().__init__()
    
    
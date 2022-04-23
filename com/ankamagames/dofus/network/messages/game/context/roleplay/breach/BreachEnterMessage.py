from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachEnterMessage(NetworkMessage):
    owner:int
    

    def init(self, owner_:int):
        self.owner = owner_
        
        super().__init__()
    
    
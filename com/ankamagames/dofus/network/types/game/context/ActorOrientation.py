from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActorOrientation(NetworkMessage):
    id:int
    direction:int
    

    def init(self, id_:int, direction_:int):
        self.id = id_
        self.direction = direction_
        
        super().__init__()
    
    
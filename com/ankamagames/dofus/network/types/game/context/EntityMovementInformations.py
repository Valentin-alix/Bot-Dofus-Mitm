from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityMovementInformations(NetworkMessage):
    id:int
    steps:list[int]
    

    def init(self, id_:int, steps_:list[int]):
        self.id = id_
        self.steps = steps_
        
        super().__init__()
    
    
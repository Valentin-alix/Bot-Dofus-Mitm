from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityInformation(NetworkMessage):
    id:int
    experience:int
    status:bool
    

    def init(self, id_:int, experience_:int, status_:bool):
        self.id = id_
        self.experience = experience_
        self.status = status_
        
        super().__init__()
    
    
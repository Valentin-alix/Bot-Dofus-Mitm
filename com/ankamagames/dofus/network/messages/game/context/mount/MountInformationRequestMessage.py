from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationRequestMessage(NetworkMessage):
    id:int
    time:int
    

    def init(self, id_:int, time_:int):
        self.id = id_
        self.time = time_
        
        super().__init__()
    
    
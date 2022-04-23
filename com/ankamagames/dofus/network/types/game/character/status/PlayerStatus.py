from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PlayerStatus(NetworkMessage):
    statusId:int
    

    def init(self, statusId_:int):
        self.statusId = statusId_
        
        super().__init__()
    
    
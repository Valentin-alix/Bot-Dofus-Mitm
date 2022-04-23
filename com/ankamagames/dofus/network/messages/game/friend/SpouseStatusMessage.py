from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpouseStatusMessage(NetworkMessage):
    hasSpouse:bool
    

    def init(self, hasSpouse_:bool):
        self.hasSpouse = hasSpouse_
        
        super().__init__()
    
    
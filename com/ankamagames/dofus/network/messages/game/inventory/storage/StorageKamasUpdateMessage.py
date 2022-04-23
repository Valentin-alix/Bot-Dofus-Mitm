from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageKamasUpdateMessage(NetworkMessage):
    kamasTotal:int
    

    def init(self, kamasTotal_:int):
        self.kamasTotal = kamasTotal_
        
        super().__init__()
    
    
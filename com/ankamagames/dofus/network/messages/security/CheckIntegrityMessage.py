from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckIntegrityMessage(NetworkMessage):
    data:list[int]
    

    def init(self, data_:list[int]):
        self.data = data_
        
        super().__init__()
    
    
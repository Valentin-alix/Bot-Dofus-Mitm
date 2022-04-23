from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseKickIndoorMerchantRequestMessage(NetworkMessage):
    cellId:int
    

    def init(self, cellId_:int):
        self.cellId = cellId_
        
        super().__init__()
    
    
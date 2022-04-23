from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseToSellListRequestMessage(NetworkMessage):
    pageIndex:int
    

    def init(self, pageIndex_:int):
        self.pageIndex = pageIndex_
        
        super().__init__()
    
    
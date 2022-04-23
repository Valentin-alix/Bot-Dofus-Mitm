from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectAveragePricesMessage(NetworkMessage):
    ids:list[int]
    avgPrices:list[int]
    

    def init(self, ids_:list[int], avgPrices_:list[int]):
        self.ids = ids_
        self.avgPrices = avgPrices_
        
        super().__init__()
    
    
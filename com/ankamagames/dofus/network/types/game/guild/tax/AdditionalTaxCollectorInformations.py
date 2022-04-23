from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AdditionalTaxCollectorInformations(NetworkMessage):
    collectorCallerName:str
    date:int
    

    def init(self, collectorCallerName_:str, date_:int):
        self.collectorCallerName = collectorCallerName_
        self.date = date_
        
        super().__init__()
    
    
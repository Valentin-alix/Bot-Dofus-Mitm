from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeReplyTaxVendorMessage(NetworkMessage):
    objectValue:int
    totalTaxValue:int
    

    def init(self, objectValue_:int, totalTaxValue_:int):
        self.objectValue = objectValue_
        self.totalTaxValue = totalTaxValue_
        
        super().__init__()
    
    
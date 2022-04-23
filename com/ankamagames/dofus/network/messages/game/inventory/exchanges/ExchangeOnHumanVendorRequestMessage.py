from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeOnHumanVendorRequestMessage(NetworkMessage):
    humanVendorId:int
    humanVendorCell:int
    

    def init(self, humanVendorId_:int, humanVendorCell_:int):
        self.humanVendorId = humanVendorId_
        self.humanVendorCell = humanVendorCell_
        
        super().__init__()
    
    
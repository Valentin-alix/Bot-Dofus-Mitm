from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SellerBuyerDescriptor(NetworkMessage):
    quantities:list[int]
    types:list[int]
    taxPercentage:int
    taxModificationPercentage:int
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    

    def init(self, quantities_:list[int], types_:list[int], taxPercentage_:int, taxModificationPercentage_:int, maxItemLevel_:int, maxItemPerAccount_:int, npcContextualId_:int, unsoldDelay_:int):
        self.quantities = quantities_
        self.types = types_
        self.taxPercentage = taxPercentage_
        self.taxModificationPercentage = taxModificationPercentage_
        self.maxItemLevel = maxItemLevel_
        self.maxItemPerAccount = maxItemPerAccount_
        self.npcContextualId = npcContextualId_
        self.unsoldDelay = unsoldDelay_
        
        super().__init__()
    
    
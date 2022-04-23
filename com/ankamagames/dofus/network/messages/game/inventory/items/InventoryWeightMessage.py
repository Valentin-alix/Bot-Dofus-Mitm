from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InventoryWeightMessage(NetworkMessage):
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    

    def init(self, inventoryWeight_:int, shopWeight_:int, weightMax_:int):
        self.inventoryWeight = inventoryWeight_
        self.shopWeight = shopWeight_
        self.weightMax = weightMax_
        
        super().__init__()
    
    
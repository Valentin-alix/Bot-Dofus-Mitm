from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ItemDurability(NetworkMessage):
    durability:int
    durabilityMax:int
    

    def init(self, durability_:int, durabilityMax_:int):
        self.durability = durability_
        self.durabilityMax = durabilityMax_
        
        super().__init__()
    
    
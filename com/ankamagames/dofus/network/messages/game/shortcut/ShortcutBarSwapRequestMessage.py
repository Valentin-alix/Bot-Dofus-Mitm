from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarSwapRequestMessage(NetworkMessage):
    barType:int
    firstSlot:int
    secondSlot:int
    

    def init(self, barType_:int, firstSlot_:int, secondSlot_:int):
        self.barType = barType_
        self.firstSlot = firstSlot_
        self.secondSlot = secondSlot_
        
        super().__init__()
    
    
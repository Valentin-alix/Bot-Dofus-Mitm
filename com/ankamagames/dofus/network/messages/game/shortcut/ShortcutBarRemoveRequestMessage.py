from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarRemoveRequestMessage(NetworkMessage):
    barType:int
    slot:int
    

    def init(self, barType_:int, slot_:int):
        self.barType = barType_
        self.slot = slot_
        
        super().__init__()
    
    
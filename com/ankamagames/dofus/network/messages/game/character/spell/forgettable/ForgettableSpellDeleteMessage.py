from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellDeleteMessage(NetworkMessage):
    reason:int
    spells:list[int]
    

    def init(self, reason_:int, spells_:list[int]):
        self.reason = reason_
        self.spells = spells_
        
        super().__init__()
    
    
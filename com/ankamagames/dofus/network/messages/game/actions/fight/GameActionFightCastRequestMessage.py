from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastRequestMessage(NetworkMessage):
    spellId:int
    cellId:int
    

    def init(self, spellId_:int, cellId_:int):
        self.spellId = spellId_
        self.cellId = cellId_
        
        super().__init__()
    
    
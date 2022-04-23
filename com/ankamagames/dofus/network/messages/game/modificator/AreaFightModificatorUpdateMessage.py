from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AreaFightModificatorUpdateMessage(NetworkMessage):
    spellPairId:int
    

    def init(self, spellPairId_:int):
        self.spellPairId = spellPairId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellVariantActivationRequestMessage(NetworkMessage):
    spellId:int
    

    def init(self, spellId_:int):
        self.spellId = spellId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellVariantActivationMessage(NetworkMessage):
    spellId:int
    result:bool
    

    def init(self, spellId_:int, result_:bool):
        self.spellId = spellId_
        self.result = result_
        
        super().__init__()
    
    
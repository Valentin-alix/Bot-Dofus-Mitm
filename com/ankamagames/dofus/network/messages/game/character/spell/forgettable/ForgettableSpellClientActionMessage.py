from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    spellId:int
    action:int
    

    def init(self, spellId_:int, action_:int):
        self.spellId = spellId_
        self.action = action_
        
        super().__init__()
    
    
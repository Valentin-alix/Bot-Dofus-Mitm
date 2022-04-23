from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightSpellCooldown(NetworkMessage):
    spellId:int
    cooldown:int
    

    def init(self, spellId_:int, cooldown_:int):
        self.spellId = spellId_
        self.cooldown = cooldown_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildSpellUpgradeRequestMessage(NetworkMessage):
    spellId:int
    

    def init(self, spellId_:int):
        self.spellId = spellId_
        
        super().__init__()
    
    
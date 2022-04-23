from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellForPreset(NetworkMessage):
    spellId:int
    shortcuts:list[int]
    

    def init(self, spellId_:int, shortcuts_:list[int]):
        self.spellId = spellId_
        self.shortcuts = shortcuts_
        
        super().__init__()
    
    
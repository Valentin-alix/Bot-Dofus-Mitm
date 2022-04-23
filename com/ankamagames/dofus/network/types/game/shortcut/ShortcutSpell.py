from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutSpell(Shortcut):
    spellId:int
    

    def init(self, spellId_:int, slot_:int):
        self.spellId = spellId_
        
        super().__init__(slot_)
    
    
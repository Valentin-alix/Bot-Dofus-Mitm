from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutEmote(Shortcut):
    emoteId:int
    

    def init(self, emoteId_:int, slot_:int):
        self.emoteId = emoteId_
        
        super().__init__(slot_)
    
    
from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


class ShortcutObjectPreset(ShortcutObject):
    presetId:int
    

    def init(self, presetId_:int, slot_:int):
        self.presetId = presetId_
        
        super().__init__(slot_)
    
    
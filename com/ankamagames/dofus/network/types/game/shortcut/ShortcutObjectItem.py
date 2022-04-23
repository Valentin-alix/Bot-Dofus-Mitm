from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


class ShortcutObjectItem(ShortcutObject):
    itemUID:int
    itemGID:int
    

    def init(self, itemUID_:int, itemGID_:int, slot_:int):
        self.itemUID = itemUID_
        self.itemGID = itemGID_
        
        super().__init__(slot_)
    
    
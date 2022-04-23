from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class SpellItem(Item):
    spellId:int
    spellLevel:int
    

    def init(self, spellId_:int, spellLevel_:int):
        self.spellId = spellId_
        self.spellLevel = spellLevel_
        
        super().__init__()
    
    
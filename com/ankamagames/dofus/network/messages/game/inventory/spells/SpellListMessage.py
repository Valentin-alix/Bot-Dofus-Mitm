from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
    


class SpellListMessage(NetworkMessage):
    spellPrevisualization:bool
    spells:list['SpellItem']
    

    def init(self, spellPrevisualization_:bool, spells_:list['SpellItem']):
        self.spellPrevisualization = spellPrevisualization_
        self.spells = spells_
        
        super().__init__()
    
    
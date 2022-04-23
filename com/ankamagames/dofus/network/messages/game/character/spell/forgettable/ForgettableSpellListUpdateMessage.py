from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem
    


class ForgettableSpellListUpdateMessage(NetworkMessage):
    action:int
    spells:list['ForgettableSpellItem']
    

    def init(self, action_:int, spells_:list['ForgettableSpellItem']):
        self.action = action_
        self.spells = spells_
        
        super().__init__()
    
    
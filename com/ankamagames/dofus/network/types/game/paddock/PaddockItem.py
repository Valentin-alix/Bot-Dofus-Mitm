from com.ankamagames.dofus.network.types.game.context.roleplay.ObjectItemInRolePlay import ObjectItemInRolePlay
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.ItemDurability import ItemDurability
    


class PaddockItem(ObjectItemInRolePlay):
    durability:'ItemDurability'
    

    def init(self, durability_:'ItemDurability', cellId_:int, objectGID_:int):
        self.durability = durability_
        
        super().__init__(cellId_, objectGID_)
    
    
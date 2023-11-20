from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.ObjectItemInRolePlay import ObjectItemInRolePlay
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.mount.ItemDurability import ItemDurability
class PaddockItem(ObjectItemInRolePlay):
	def __init__(self, durability:ItemDurability, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.durability=durability
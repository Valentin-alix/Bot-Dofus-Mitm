from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.Item import Item
if TYPE_CHECKING:
	...
class ObjectItemGenericQuantity(Item):
	def __init__(self, objectGID:int, quantity:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectGID=objectGID
		self.quantity=quantity
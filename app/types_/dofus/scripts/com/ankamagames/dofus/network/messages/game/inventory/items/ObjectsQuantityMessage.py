from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity
class ObjectsQuantityMessage:
	def __init__(self, objectsUIDAndQty:list[ObjectItemQuantity]):
		self.objectsUIDAndQty=objectsUIDAndQty
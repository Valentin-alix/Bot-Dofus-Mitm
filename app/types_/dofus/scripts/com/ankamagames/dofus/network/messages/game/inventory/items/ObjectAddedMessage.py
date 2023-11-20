from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class ObjectAddedMessage:
	def __init__(self, object:ObjectItem, origin:int):
		self.object=object
		self.origin=origin
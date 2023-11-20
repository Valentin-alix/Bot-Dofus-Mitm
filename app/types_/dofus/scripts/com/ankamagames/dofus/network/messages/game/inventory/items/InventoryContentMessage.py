from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class InventoryContentMessage:
	def __init__(self, objects:list[ObjectItem], kamas:int):
		self.objects=objects
		self.kamas=kamas
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class StorageObjectsUpdateMessage:
	def __init__(self, objectList:list[ObjectItem]):
		self.objectList=objectList
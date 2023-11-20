from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
class TaxCollectorEquipmentUpdateMessage:
	def __init__(self, uniqueId:float, object:ObjectItem, added:bool, characteristics:CharacterCharacteristics):
		self.uniqueId=uniqueId
		self.object=object
		self.added=added
		self.characteristics=characteristics
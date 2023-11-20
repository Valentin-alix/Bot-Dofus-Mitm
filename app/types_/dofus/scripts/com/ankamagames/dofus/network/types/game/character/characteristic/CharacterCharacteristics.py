from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
class CharacterCharacteristics:
	def __init__(self, characteristics:list[CharacterCharacteristic]):
		self.characteristics=characteristics
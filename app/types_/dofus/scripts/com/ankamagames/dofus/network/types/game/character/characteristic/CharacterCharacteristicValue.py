from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
if TYPE_CHECKING:
	...
class CharacterCharacteristicValue(CharacterCharacteristic):
	def __init__(self, total:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.total=total
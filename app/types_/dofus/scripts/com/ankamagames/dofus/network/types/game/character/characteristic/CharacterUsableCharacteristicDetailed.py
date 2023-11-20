from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
if TYPE_CHECKING:
	...
class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
	def __init__(self, used:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.used=used
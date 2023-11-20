from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
if TYPE_CHECKING:
	...
class CharacterCharacteristicForPreset(SimpleCharacterCharacteristicForPreset):
	def __init__(self, stuff:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.stuff=stuff
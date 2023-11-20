from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
if TYPE_CHECKING:
	...
class CharacterMinimalInformations(CharacterBasicMinimalInformations):
	def __init__(self, level:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level=level
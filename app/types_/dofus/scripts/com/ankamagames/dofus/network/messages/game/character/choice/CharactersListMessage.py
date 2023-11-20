from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
class CharactersListMessage:
	def __init__(self, characters:list[CharacterBaseInformations]):
		self.characters=characters
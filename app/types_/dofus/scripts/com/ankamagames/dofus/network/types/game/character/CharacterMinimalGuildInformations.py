from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
	def __init__(self, guild:BasicGuildInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guild=guild
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterCapabilitiesMessage:
	def __init__(self, guildEmblemSymbolCategories:int):
		self.guildEmblemSymbolCategories=guildEmblemSymbolCategories
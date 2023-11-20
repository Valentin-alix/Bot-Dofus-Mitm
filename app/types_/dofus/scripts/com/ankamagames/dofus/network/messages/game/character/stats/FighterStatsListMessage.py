from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
class FighterStatsListMessage:
	def __init__(self, stats:CharacterCharacteristicsInformations):
		self.stats=stats
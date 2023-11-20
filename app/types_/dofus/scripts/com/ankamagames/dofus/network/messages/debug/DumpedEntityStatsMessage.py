from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
class DumpedEntityStatsMessage:
	def __init__(self, actorId:float, stats:CharacterCharacteristics):
		self.actorId=actorId
		self.stats=stats
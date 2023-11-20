from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
class RefreshCharacterStatsMessage:
	def __init__(self, fighterId:float, stats:GameFightCharacteristics):
		self.fighterId=fighterId
		self.stats=stats